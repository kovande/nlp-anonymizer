# models.py

import spacy
from transformers import pipeline

_spacy_model = None
_transformer_pipeline = None


def get_spacy():
    """
    Lazy-load spaCy model.
    This prevents expensive reloads when the function is called multiple times
    (important for APIs / Streamlit apps).
    """
    global _spacy_model
    if _spacy_model is None:
        _spacy_model = spacy.load("en_core_web_sm")
    return _spacy_model


def get_transformer():
    """
    Lazy-load HuggingFace NER pipeline.
    """
    global _transformer_pipeline
    if _transformer_pipeline is None:
        _transformer_pipeline = pipeline(
            "ner",
            model="dslim/bert-base-NER",
            aggregation_strategy="simple"
        )
    return _transformer_pipeline