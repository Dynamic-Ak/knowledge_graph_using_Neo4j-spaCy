# Query Examples

## 1. List all extracted entities
MATCH (n) RETURN n;

## 2. Find models and their tasks
MATCH (m)-[:USES]->(t)
RETURN m.name, t.name;

## 3. Find datasets used in emotion analysis
MATCH (d)-[:USED_IN]->(t)
RETURN d.name, t.name;

## 4. Show complete knowledge graph
MATCH (n)-[r]->(m)
RETURN n,r,m;
