from neo4j import GraphDatabase

driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j", "neo4j123")
)

# Load entities extracted by spaCy
with open("entities.txt", "r", encoding="utf-8") as f:
    entities = [e.strip() for e in f.readlines() if e.strip()]

def build_graph(tx):
    # Create entity nodes
    for e in entities:
        tx.run("MERGE (:Entity {name:$name})", name=e)

    # Rule-based relationships
    for e in entities:
        if "BERT" in e or "RoBERTa" in e or "DeBERTa" in e:
            tx.run("""
                MATCH (m:Entity {name:$model}),
                      (t:Entity {name:"Emotion Analysis"})
                MERGE (m)-[:USES]->(t)
            """, model=e)

        if "GoEmotions" in e:
            tx.run("""
                MATCH (d:Entity {name:$ds}),
                      (t:Entity {name:"Emotion Analysis"})
                MERGE (d)-[:USED_IN]->(t)
            """, ds=e)

        if "Emotion Drift" in e:
            tx.run("""
                MATCH (e:Entity {name:$e}),
                      (t:Entity {name:"Emotion Analysis"})
                MERGE (e)-[:IMPROVES]->(t)
            """, e=e)

with driver.session() as session:
    session.execute_write(build_graph)

print("✅ Entities and relations created successfully")
