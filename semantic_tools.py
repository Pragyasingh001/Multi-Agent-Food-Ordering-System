import os
import json
from neo4j import GraphDatabase
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

load_dotenv()

URI = os.getenv("NEO4J_URI")
USER = os.getenv("NEO4J_USER")
PASSWORD = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))
model = SentenceTransformer("all-MiniLM-L6-v2")


def _build_dish_text(row: dict) -> str:
    ingredients = ", ".join([x for x in row.get("ingredients", []) if x])
    return (
        f"Dish: {row.get('dish_name', '')}. "
        f"Cuisine: {row.get('cuisine', '')}. "
        f"Category: {row.get('category', '')}. "
        f"Type: {row.get('dish_type', '')}. "
        f"Nutrition: {row.get('nutrition', '')}. "
        f"Ingredients: {ingredients}. "
        f"Price: {row.get('price', '')}."
    )


def create_dish_embeddings():
    try:
        with driver.session() as session:
            result = session.run("""
                MATCH (d:Dish)
                OPTIONAL MATCH (d)-[:ORIGINATES_FROM]->(c:Cuisine)
                OPTIONAL MATCH (d)-[:BELONGS_TO]->(cat:Category)
                OPTIONAL MATCH (d)-[:HAS_TYPE]->(t:Type)
                OPTIONAL MATCH (d)-[:NUTRITIONAL_BENEFIT]->(n:Nutrition)
                OPTIONAL MATCH (d)-[:COSTS]->(p:Price)
                OPTIONAL MATCH (d)-[:HAS_INGREDIENT]->(i:Ingredient)
                RETURN d.name AS dish_name,
                       c.name AS cuisine,
                       cat.name AS category,
                       t.name AS dish_type,                 
                       n.label AS nutrition,
                       p.value AS price,
                       collect(i.name) AS ingredients
            """)

            rows = [r.data() for r in result]

            for row in rows:
                text = _build_dish_text(row)
                embedding = model.encode(text).tolist()

                session.run("""
                    MATCH (d:Dish {name: $dish_name})
                    SET d.embedding_text = $embedding_text,
                        d.embedding = $embedding
                """, {
                    "dish_name": row["dish_name"],
                    "embedding_text": text,
                    "embedding": embedding
                })

            return json.dumps({
                "status": "success",
                "count": len(rows),
                "message": "Embeddings created for all dishes"
            })

    except Exception as e:
        return json.dumps({"error": str(e)})


def semantic_food_search(user_query: str):
    top_k = 5
    min_score = 0.65
    try:
        query_embedding = model.encode(user_query).tolist()

        with driver.session() as session:
            result = session.run("""
                CALL db.index.vector.queryNodes('dish_embedding_index', $top_k, $embedding)
                YIELD node, score
                WHERE score >= $min_score
                OPTIONAL MATCH (node)-[:COSTS]->(p:Price)
                RETURN node.name AS dish_name, p.value AS price, score
                ORDER BY score DESC
            """, {
                "top_k": top_k,
                "embedding": query_embedding,
                "min_score": min_score
            })

            rows = [r.data() for r in result]

            if not rows:
                return "No matching dish found."

            lines = ["## Matching Dishes", ""]
            for row in rows:
                price = row["price"] if row["price"] is not None else "N/A"
                lines.append(f"- **{row['dish_name']}** — ₹{price}")
            return "\n".join(lines)

    except Exception as e:
        return f"Error in semantic search: {str(e)}"
