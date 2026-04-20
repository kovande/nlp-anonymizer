# utils.py

import re

def apply_regex(text, patterns):
    """
    Apply regex-based replacements for structured sensitive data.
    Example: emails, phone numbers, IBANs, etc.
    """
    for tag, pattern in patterns.items():
        text = re.sub(pattern, tag, text)
    return text


def replace_entities(text, entities, label_map, start_key, end_key, label_key):
    """
    Replace entity spans in text with anonymization tags.

    Important:
    - We iterate in reverse order to avoid index shifting problems.
      (Replacing earlier text would otherwise change positions of later entities.)
    """
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