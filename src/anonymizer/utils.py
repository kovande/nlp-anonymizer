# utils.py

import re

def apply_regex(text, patterns):
    for tag, pattern in patterns.items():
        text = re.sub(pattern, tag, text)
    return text


def replace_entities(text, entities, label_map, start_key, end_key, label_key):
    for ent in reversed(entities):
        label = ent[label_key]
        if label in label_map:
            text = (
                text[:ent[start_key]]
                + label_map[label]
                + text[ent[end_key]:]
            )
    return text

def replace_keywords(text, keywords, tag):
    for kw in keywords:
        pattern = rf"\b{kw}\b"
        text = re.sub(pattern, tag, text, flags=re.IGNORECASE)
    return text