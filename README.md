# knowledge_graph_using_Neo4j-spaCy


## Overview

This project converts a research paper into a **knowledge graph** using NLP.
Important entities are extracted from the paper and stored in **Neo4j**, where relationships between them can be visualized and queried.

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
