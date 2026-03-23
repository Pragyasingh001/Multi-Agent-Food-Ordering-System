import os
import json
from neo4j import GraphDatabase
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

load_dotenv()
URI = os.getenv("NEO4J_URI")
USER = os.getenv("NEO4J_USER")
PASSWORD = os.getenv("NEO4J_PASSWORD")
AUTH = (USER, PASSWORD)

def get_schema():
    """Retrieves the graph schema labels and relationships dynamically."""
    driver = GraphDatabase.driver(URI, auth=AUTH)
    print("SHOW SCHEMA")
    try:
        with driver.session() as session:
            labels = session.run("CALL db.labels()").to_df()[0].tolist()
            rels = session.run("CALL db.relationshipTypes()").to_df()[0].tolist()
            return json.dumps({"labels": labels, "relationships": rels})
    except Exception as e:
        return json.dumps({"error": str(e)})
    finally:
        driver.close()

def query_food_graph(query: str):
    """Run a Cypher query on the food graph. Use for structured queries like menu, price, cuisine, ingredients."""
    driver = GraphDatabase.driver(URI, auth=AUTH)
    try:
        with driver.session() as session:
            clean_query = query.replace("```cypher", "").replace("```", "").strip()
            result = session.run(clean_query)
            data = [record.data() for record in result]
            if not data:
                return "No items found."
            first_row = data[0]
            if isinstance(first_row, dict) and "d.name" in first_row and "p.value" in first_row:
                lines = ["## Our Menu", ""]
                for row in data:
                    lines.append(f"- **{row['d.name']}** — ₹{row['p.value']}")
                return "\n".join(lines)
            return json.dumps(data, indent=2, default=str)
    except Exception as e:
        return f"Error running query: {str(e)}"
    finally:
        driver.close()

def execute_graph_transaction(query: str, params: dict = {}):
    """Executes a Cypher transaction. Used for placing orders and calculating bills."""
    driver = GraphDatabase.driver(URI, auth=AUTH)
    try:
        with driver.session() as session:
            result = session.run(query, params or {})
            data = [record.data() for record in result]
            return json.dumps(data)
    except Exception as e:
        return json.dumps({"error": str(e), "status": "failed"})
    finally:
        driver.close()

def close_guest_session(customer_name: str = "Guest"):
    """Removes the guest session. Call only when user explicitly says goodbye."""
    query = "MATCH (g:Guest {name: $name}) DETACH DELETE g"
    return execute_graph_transaction(query, {"name": customer_name})
