import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import RAW_DATA_PATH, PROCESSED_DATA_PATH
from src.ingestion.text_loader import load_text
from src.preprocessing.cleaner import clean_text, split_sentences
from src.nlp.entity_extractor import extract_entities
from src.nlp.relation_extractor import extract_relations
from src.graph.neo4j_handler import Neo4jHandler



def run_preprocessing():
    raw_text = load_text(RAW_DATA_PATH)
    cleaned = clean_text(raw_text)
    sentences = split_sentences(cleaned)

    with open(PROCESSED_DATA_PATH, "w", encoding="utf-8") as f:
        for i, s in enumerate(sentences):
            f.write(f"{i+1}|{s}\n")

    print("Preprocessing completed.")

def load_processed_sentences():
    sentences = []
    with open(PROCESSED_DATA_PATH, "r", encoding="utf-8") as f:
        for line in f:
            sid, text = line.strip().split("|", 1)
            sentences.append((int(sid), text))
    return sentences

if __name__ == "__main__":
    run_preprocessing()
    sentences = load_processed_sentences()
    entities = extract_entities(sentences)
    relations = extract_relations(sentences, entities)
    db = Neo4jHandler()

    for r in relations:
        db.create_relation(r["source"], r["relation"], r["target"])

    db.close()
    print("Graph created in Neo4j.")