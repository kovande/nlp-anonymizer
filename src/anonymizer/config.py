# config.py

REGEX_PATTERNS = {
    "<IBAN>": r"\b[A-Z]{2}\d{2}(?:\s?\d{4}){3}\b",
    "<SSN>": r"\b\d{2}\.\d{2}\.\d{2}-\d{3}\.\d{2}\b|\b\d{3}-\d{2}-\d{4}\b",
    "<EMAIL_ADDRESS>": r"\b[\w\.-]+@[\w\.-]+\.\w+\b",
    "<URL>": r"https?://\S+|www\.\S+",
    "<PHONE_NUMBER>": r"\+?\d[\d\s\-\(\)]{7,}\d",
}

SPACY_LABEL_MAP = {
    "PERSON": "<PERSON>",
    "ORG": "<ORG>",
    "GPE": "<LOCATION>",
    "LOC": "<LOCATION>",
    "DATE": "<DATE_TIME>",
    "MONEY": "<AMOUNT>",
}

TRANSFORMER_LABEL_MAP = {
    "PER": "<PERSON>",
    "ORG": "<ORG>",
    "LOC": "<LOCATION>",
    "MISC": "<LOCATION>",
}

JOB_TITLES = [
    "engineer", "data scientist", "manager", "ceo",
    "software engineer", "doctor", "president"
]

UNIVERSITY_KEYWORDS = [
    "university", "college", "institute", "school"
]