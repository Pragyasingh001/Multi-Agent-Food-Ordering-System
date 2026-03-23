from neo4j import GraphDatabase
import os
from neo4j import GraphDatabase
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

URI = os.getenv("NEO4J_URI")
USER = os.getenv("NEO4J_USER")
PASSWORD = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(
    os.getenv("NEO4J_URI"),
    auth=(os.getenv("NEO4J_USER"), os.getenv("NEO4J_PASSWORD"))
)

cypher = Path("learning-cypher-query.md").read_text(encoding="utf-8")

# Split into individual statements by semicolon
statements = [s.strip() for s in cypher.split(";") if s.strip()]

with driver.session() as session:
    for stmt in statements:
        lines = [ln for ln in stmt.splitlines() if not ln.strip().startswith("//")]
        cleaned = "\n".join(lines).strip()
        if cleaned:
            session.run(cleaned)

print("✅ Database seeded")



