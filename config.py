# NLP
SPACY_MODEL = "en_core_web_sm"
ENTITY_TYPES = ["PERSON", "ORG", "GPE", "DATE"]

# Relations we will extract
RELATION_TYPES = ["FOUNDED", "CEO_OF", "HEADQUARTERED_IN", "BASED_IN"]

# Paths
RAW_DATA_PATH = "data/raw_text/tech_articles.txt"
PROCESSED_DATA_PATH = "data/processed/processed_sentences.txt"

# Neo4j
NEO4J_URI = "neo4j+ssc://14fcb965.databases.neo4j.io"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "goilQUR5Qz5tMu-FpbFGMNN1JSGQUT-85cB73Ab2wNY"
