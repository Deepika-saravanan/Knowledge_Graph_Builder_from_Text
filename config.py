# NLP
SPACY_MODEL = "en_core_web_sm"
ENTITY_TYPES = ["PERSON", "ORG", "GPE", "DATE"]

# Relations we will extract
RELATION_TYPES = ["FOUNDED", "CEO_OF", "HEADQUARTERED_IN", "BASED_IN"]

# Paths
RAW_DATA_PATH = "data/raw_text/company_tech_articles.txt"
PROCESSED_DATA_PATH = "data/processed/processed_sentences.txt"

# Neo4j
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "password"
