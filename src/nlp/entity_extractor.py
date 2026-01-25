import spacy
from config import SPACY_MODEL, ENTITY_TYPES

nlp = spacy.load(SPACY_MODEL)

def extract_entities(sentences: list):
    entities = []

    for sentence_id, text in sentences:
        doc = nlp(text)
        for ent in doc.ents:
            if ent.label_ in ENTITY_TYPES:
                entities.append({
                    "text": ent.text,
                    "label": ent.label_,
                    "sentence_id": sentence_id
                })

    return entities
