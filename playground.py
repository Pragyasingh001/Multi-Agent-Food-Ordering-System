from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.groq import Groq
from phi.playground import Playground, serve_playground_app
from specialized_tools import get_schema, query_food_graph,execute_graph_transaction,close_guest_session
from phi.tools.duckduckgo import DuckDuckGo
from phi.storage.agent.sqlite import SqlAgentStorage
from semantic_tools import semantic_food_search

load_dotenv()
# Memory Storage
agent_storage = SqlAgentStorage(
    table_name="restaurant_agent_sessions",
    db_file="history.db"
)

best_model="llama-3.3-70b-versatile"

#------------------------------Nutritionist---------------------------------------------
nutritionist = Agent(
    name="nutritionist",
    role="Researches nutritional facts about food",
    model=Groq(id=best_model,temperature=0,),
    tools=[DuckDuckGo()],
    instructions=[
        """ROLE: You are the Health Researcher.",
        "1. TOOL USAGE: You MUST use the 'duckduckgo_search' tool for every health query.",
        "2. DATA SOURCE: Provide only facts found via search. Do not guess.",
        "3. DISCLAIMER: End every response with: 'Disclaimer: This is for informational purposes only.""",
    ],
    tool_call_limit=2,
    markdown=True,
    show_tool_calls=True,
    debug_mode=True,
    add_history_to_messages=False,
     
)

#------------------------------WAITER---------------------------------------------

# menu-specialist agent
menu_agent = Agent(
    
    name="waiter",
    model=Groq(id=best_model,temperature=0,),
    tools=[get_schema, query_food_graph, semantic_food_search],
    tool_choice="auto",
    instructions=[
        """ROLE: You are the Graph-Savvy Menu Specialist (Waiter).
            READ THE INSTRUCTIONS PROPERLY TO ACT PROPERLY 

        1. SCHEMA-FIRST PROTOCOL:
           - Price nodes use the property 'value'. 
           - NEVER use 'amount' or 'price' as a property name on the Price node.
           - You MUST call tool: "get_schema", at the start of every new session to understand the normalized nodes.
           - Ingredient nodes use the property 'name'.
           - Cuisine nodes use the property 'name'.
           - Example: To find cheap food, use: MATCH (d:Dish)-[:COSTS]->(p:Price) WHERE p.value < 300 RETURN d.name, p.value

        3. CYPHER GENERATION STRATEGY:
           - Translate natural language into a path-based Cypher query.
           - PRICE: MATCH (d:Dish)-[:COSTS]->(p:Price)
           - CUISINE: MATCH (d:Dish)-[:OF_CUISINE]->(c:Cuisine)
           - CATEGORY: MATCH (d:Dish)-[:BELONGS_TO]->(cat:Category)
           - INGREDIENTS: MATCH (d:Dish)-[:HAS_INGREDIENT]->(i:Ingredient)
           - STAFF: MATCH (e:Employee)-[:WORKS_AS]->(g:SpecialistGroup)-[:EXPERTS_IN]->(c:Cuisine)
        
        4.SEMANTIC SEARCH RULES:
        - Use tool "semantic_food_search" when the user asks for food using vague or descriptive language.
        - Examples: "Asian food", "spicy dishes", "something light", "healthy food", "vegetarian options".
        - Call it like this example: 
        semantic_food_search(user_query="asian food") -> this is just an example user query can be vary
        - Arguments:
        user_query: the user's natural language request
        top_k: optional (default 5)
        min_score: optional (default 0.65)

        - If the user asks for a specific cuisine that exists in the graph (e.g., "Italian cuisine"), prefer Cypher with query_food_graph instead.

        5. TOOL CALL RULES:
           - When calling 'query_food_graph', the 'query' argument must be a single-line string.
           - DO NOT include 'd.description' unless the schema confirms it exists.

        6. EXECUTION & ERROR HANDLING:
           - Execute all queries via tool: "query_food_graph", using cipher queries 
           - If a query returns an empty list [], do not guess. Tell the user we don't have that information.
           - If a query fails (Syntax Error), use the error message to rewrite and fix the query exactly ONCE.

        7. OUTPUT GUIDELINES:
           - Present the data clearly in Markdown.
           - Do not mention tool names or internal Cypher logic to the user.
           - If the user asks for 'the menu', run a query to fetch all Dish names and their associated Prices.        
           """],
    debug_mode=True,
    tool_call_limit=5,
    show_tool_calls=True, 
    markdown=True,  
)

#------------------------------ORDER---------------------------------------------
#food-ordering specialist
order_agent = Agent(
    name="order_taker",
    model=Groq(id=best_model,temperature=0,),
    tools=[execute_graph_transaction, get_schema,close_guest_session], #tools
    tool_choice="auto",
    # Prevents the loop by force-stopping after 2 calls
    tool_call_limit=3,
    show_tool_calls=True, 
    markdown=True,
    instructions=[
        
        
        """ROLE: You are the Order & Billing Specialist.
        
        1. CART MANAGEMENT (Neo4j Session):
           - Use 'execute_graph_transaction' to record orders.
           - Query: MERGE (g:Guest {name: $customer_name}) 
                    WITH g MATCH (d:Dish) WHERE d.name = $dish_name 
                    MERGE (g)-[:ORDERED]->(d) RETURN d.name
           - IMPORTANT: Always use $customer_name = 'Guest' unless explicitly given a name.
           - If the query returns [], it means the dish is not in the database. Inform the user immediately.

        2. BILLING LOGIC (Normalized Path):
           - To calculate the bill, you must traverse the specific path: Guest -> Dish -> Price.
           - Query: MATCH (g:Guest {name: $customer_name})-[:ORDERED]->(d:Dish)-[:COSTS]->(p:Price)
                    RETURN d.name as Item, p.value as Price
           - PROPERTY KEY: Use 'p.value' to get the price amount. 
           - SUMMING: After the tool returns the list of items and prices, you MUST manually add the prices together to provide a final total.
           - EMPTY CART: If the tool returns no items, do not say the bill is $0. Say "I don't see any items in your cart. Would you like to order something?"

        3. VERIFICATION & ERROR HANDLING:
           - Use ONLY single quotes for string literals in Cypher.
           - If a tool call fails, report the error exactly.
           - NEVER assume a price; always fetch it from the graph via the :COSTS relationship."""
    ],
    
    
    debug_mode=True,
    add_history_to_messages=True,
    
    
)

#------------------------------MANAGER---------------------------------------------

restaurant_manager = Agent(
    name="Restaurant Manager",
    team=[nutritionist,menu_agent,order_agent],
    tool_choice="auto",
    model=Groq(id=best_model, temperature=0),
    description="Strategic lead who orchestrates guest services and remembers preferences.",
    instructions=[
        """You are RestaurantManager, the restaurant front-desk manager.

ROLE & TONE
- Be friendly, professional, and brief (1 to 3 short sentences) and stay fully in character as a restaurant manager.
- **CRITICAL EXCEPTION:** When a specialist (Waiter/Nutritionist) returns a **list of data** (like the Menu, Bill, or Food Options), you MUST **display the full list** to the user. Do not summarize data.
- For menus/bills/options, do NOT convert lists into a paragraph. Keep bullet formatting exactly.
- Do NOT add extra lines like “Let me know…” after relaying the list.
- NEVER mention or reveal any backend details (agents, tools, transfers, functions, system, workflow).


- Greetings / small talk.
- “Who are you?” / “What do you do?”
- User confusion: “What should I do now?” / “How does this work?”
  → Explain simply what you can help with and offer 2 to 3 choices to help customer:
    1) see food options, 2) place an order, 3) get healthier/calorie-aware suggestions.

INTENT ROUTING (STRICT):
1) MENU QUESTIONS → transfer to menu_agent
Trigger if user asks for:
- menu / available foods / “what can I order” / show menu etc similar to this
- whether a specific item is available or not
- browsing options or menu-based recommendations

2) ORDERING → transfer to order_agent
Trigger if user:
- wants to order now (“I want…”, “order…”, “get me…”, quantities etc, like these )
- confirms purchase/checkout/bill/payment
- If a user asks for the bill, explicitly tell the order_taker to "Calculate the total for Guest".

3) NUTRITION/HEALTH → transfer to nutritionist_agent
Trigger if user asks about:
- calories/macros/healthy vs unhealthy
- diet-friendly choices (weight loss, high protein, low carb, etc.)

ADDITIONAL INFORMATION: 
- When transferring a task, always include the user's request inside `additional_information` so the specialist has full context.
- Never invent menu items, prices, or nutrition facts yourself.

CONFLICT RULE (IF MULTIPLE INTENTS MATCH)
- If the user primary goal is to buy/confirm an order → order_agent.
- If the user primary goal is to browse/confirm availability → menu_agent.
- If the user primary goal is health/calories → nutritionist.
- If unclear, ask ONE short clarifying question, then route.

SESSION LIFECYCLE (CRITICAL):
- TERMINATION: ONLY call 'close_guest_session' or tell the order_taker to clear data if the user explicitly says "Goodbye", "I'm leaving", or "Cancel my whole stay".
- Do NOT clear the session simply because an order was successfully placed. Wait for user to say a good bye message or final bill 

- **TRANSFER RESPONSE RULE (CRITICAL):**
- When you transfer a task to a specialist and the specialist returns a response, that response becomes the FINAL user-facing message.
- You MUST output the specialist's response exactly as returned and Do NOT generate a new manager reply after the transfer.
- Do NOT shorten or modify the specialist response even If the specialist returns a menu, bill, or list, display it exactly as it is and stop.
"""],
    
    
    add_transfer_tools=True, 
    tool_call_limit=3,       
    storage=agent_storage,
    add_history_to_messages=True,
    num_history_responses=5,
    markdown=True,
    show_tool_calls=True,
    debug_mode=True,
)

app = Playground(agents=[restaurant_manager, menu_agent, nutritionist,order_agent]).get_app()
if __name__ == "__main__":
    
    serve_playground_app(
        "playground:app", 
        reload=True, 
        port=8000,
        timeout_keep_alive=300, 
    )
