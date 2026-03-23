# Agentic Food Ordering System

A multi-agent AI system that converts natural language food requests into structured workflows for menu discovery, ordering, and billing using graph queries and semantic search.

Overview
This project simulates a real-world restaurant assistant powered by multiple AI agents.  
It understands user intent, routes tasks to specialized agents, retrieves structured data, and executes actions like placing orders and generating bills.

Key Features
- Multi-agent architecture (Manager, Menu, Ordering, Nutrition agents)  
- Natural language → structured workflow execution  
- Graph-based querying using Neo4j : Cypher queries  
- Semantic search for vague queries (e.g., “something healthy”)  
- End-to-end order execution and billing  
- Session memory and context handling  
- Reliable, non-hallucinated outputs using tool constraints

Architecture
- **Manager Agent**: Handles user interaction and routes tasks  
- **Menu Agent**: Retrieves food options using graph queries  
- **Order Agent**: Executes orders and calculates billing  
- **Nutrition Agent**: Provides health-related insights

Tech Stack
- Python  
- Neo4j (Graph Database)  
- Sentence Transformers (Semantic Search)  
- PhiData (Agent framework)  
