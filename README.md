# knowledge_graph_using_Neo4j-spaCy


## Overview
In this project, I built a system that converts an unstructured research paper into a structured Knowledge Graph. The research paper is first processed using Python and spaCy to automatically extract important entities such as models, datasets, and research concepts. Since raw NLP extraction can produce noisy results, rule-based filtering is applied to retain only meaningful academic entities. The cleaned entities are stored as nodes in a Neoj graph database. Semantic relationships such as USED_FOR, DATASET_FOR, BASED_ON, and PART_OF are created automatically using rule-based logic, transforming isolated entities into a connected knowledge graph that represents the structure of the research. Neoj is containerized using Docker to ensure easy deployment and environment consistency. The final graph can be queried and visually explored using Cypher queries, allowing clear understanding of how models, datasets, and concepts are connected within the research paper.
---

## Tech Stack

* Python
* spaCy (NLP)
* Neo4j
* Docker

---

## Project Structure

```
ready_project/
├── research_paper.pdf
├── data.txt
├── extract_entities.py
├── neo4j_upload.py
├── docker-compose.yml
├── entities.txt
```

---

## How It Works

1. The research paper is converted into text.
2. spaCy automatically extracts important entities.
3. Extracted entities are cleaned and stored in Neo4j.
4. Rule-based logic creates relationships between entities.
5. The knowledge graph is visualized using Neo4j Browser.

---

## Relationships Created

* USED_FOR
* DATASET_FOR
* BASED_ON
* PART_OF

---

## How to Run

### Start Neo4j

```bash
docker-compose up
```

Open:

```
http://localhost:7474
```

---

### Extract Entities

```bash
python extract_entities.py
```

---

### Upload to Neo4j

```bash
python neo4j_upload.py
```

---

### View Graph

```cypher
MATCH (n)-[r]->(m)
RETURN n, r, m;
```

---

## Purpose

This project helps in understanding and visualizing how models, datasets, and concepts are connected in a research paper.

---

## Author

Abhishek Kumar
