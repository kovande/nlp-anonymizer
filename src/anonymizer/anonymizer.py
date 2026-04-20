from .config import REGEX_PATTERNS, SPACY_LABEL_MAP, TRANSFORMER_LABEL_MAP, JOB_TITLES, UNIVERSITY_KEYWORDS
from .utils import apply_regex, replace_entities, replace_keywords
from .models import get_spacy, get_transformer

def anonymize_spacy(text: str) -> str:
    """
    Anonymize sensitive data using:
    1. Regex (for structured patterns like email, IBAN, phone)
    2. Keyword replacement (for job titles and universities)
    3. spaCy NER (for named entities like PERSON, ORG, LOCATION)

    Order matters: regex and keyword replacements run first to avoid confusing the NLP model.
    """
    # Step 1: replace structured patterns (fast + precise)
    text = apply_regex(text, REGEX_PATTERNS)

    # Step 2: replace keywords (also fast + precise)
    text = replace_keywords(text, JOB_TITLES, "<JOB_TITLE>")
    text = replace_keywords(text, UNIVERSITY_KEYWORDS, "<UNIVERSITY>")

    # Step 3: apply spaCy NER
    nlp = get_spacy()
    doc = nlp(text)

    # Convert spaCy entities into a simple dict format
    entities = [
        {"start": ent.start_char, "end": ent.end_char, "label": ent.label_}
        for ent in doc.ents
    ]

    # Replace detected entities with placeholders based on the label map
    return replace_entities(
        text,
        entities,
        SPACY_LABEL_MAP,
        start_key="start",
        end_key="end",
        label_key="label",
    )

def anonymize_transformer(text: str) -> str:
    """
    Same logic as spaCy version, but using a transformer NER model.
    """
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