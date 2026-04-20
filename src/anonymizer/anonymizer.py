from .config import REGEX_PATTERNS, SPACY_LABEL_MAP, TRANSFORMER_LABEL_MAP, JOB_TITLES, UNIVERSITY_KEYWORDS
from .utils import apply_regex, replace_entities, replace_keywords
from .models import get_spacy, get_transformer

def anonymize_spacy(text: str) -> str:
    text = apply_regex(text, REGEX_PATTERNS)
    text = replace_keywords(text, JOB_TITLES, "<JOB_TITLE>")
    text = replace_keywords(text, UNIVERSITY_KEYWORDS, "<UNIVERSITY>")

    nlp = get_spacy()
    doc = nlp(text)

    entities = [
        {"start": ent.start_char, "end": ent.end_char, "label": ent.label_}
        for ent in doc.ents
    ]

    return replace_entities(
        text,
        entities,
        SPACY_LABEL_MAP,
        start_key="start",
        end_key="end",
        label_key="label",
    )

def anonymize_transformer(text: str) -> str:
    text = apply_regex(text, REGEX_PATTERNS)
    text = replace_keywords(text, JOB_TITLES, "<JOB_TITLE>")
    text = replace_keywords(text, UNIVERSITY_KEYWORDS, "<UNIVERSITY>")

    ner = get_transformer()
    entities = ner(text)

    return replace_entities(
        text,
        entities,
        TRANSFORMER_LABEL_MAP,
        start_key="start",
        end_key="end",
        label_key="entity_group",
    )