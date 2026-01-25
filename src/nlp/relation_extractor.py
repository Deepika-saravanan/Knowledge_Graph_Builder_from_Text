def extract_relations(sentences, entities):
    relations = []

    entity_map = {}
    for e in entities:
        entity_map.setdefault(e["sentence_id"], []).append(e)

    for sid, text in sentences:
        ents = entity_map.get(sid, [])
        if len(ents) < 2:
            continue

        for i in range(len(ents) - 1):
            e1 = ents[i]
            e2 = ents[i + 1]

            relation = {
                "source": e1["text"],
                "target": e2["text"],
                "relation": "RELATED_TO",
                "sentence_id": sid
            }
            relations.append(relation)

    return relations
