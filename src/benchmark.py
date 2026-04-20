#from sklearn.metrics import precision_score, recall_score, f1_score

import pandas as pd
from src.anonymizer import anonymize_spacy, anonymize_transformer

def simple_evaluation(predictions, references):
    """
    Exact string match accuracy.

    Note:
    This is very strict and often misleading for NLP tasks,
    since small formatting differences count as errors.
    """
    correct = sum(p == r for p, r in zip(predictions, references))
    accuracy = correct / len(predictions)
    return accuracy

def extract_tags(text):
    """Extract anonymization tags like <PERSON>, <ORG> from text."""
    return set([word for word in text.split() if word.startswith("<")])

def entity_level_score(pred, ref):
    """
    Compute an F1-like score based on detected tags.

    The function compares only the presence of tags (e.g. <PERSON>, <ORG>)
    and ignores their position or frequency in the text.

    Example:
        ref  = "<PERSON> works at <ORG> in <LOCATION>"
        pred = "<PERSON> works at <ORG>"

        pred_tags = {"<PERSON>", "<ORG>"}
        ref_tags  = {"<PERSON>", "<ORG>", "<LOCATION>"}

        precision = 2/2 = 1.0   (all predicted tags are correct)
        recall    = 2/3 ≈ 0.67  (missed <LOCATION>)
        F1        ≈ 0.80

    Note:
        - Does NOT consider positions of entities
        - Does NOT account for multiple occurrences of the same tag
        - Useful for quick evaluation, but not a full NER metric
    """
    pred_tags = extract_tags(pred)
    ref_tags = extract_tags(ref)

    if not ref_tags:
        return 1.0

    precision = len(pred_tags & ref_tags) / max(len(pred_tags), 1)
    recall = len(pred_tags & ref_tags) / len(ref_tags)

    if precision + recall == 0:
        return 0.0

    return 2 * (precision * recall) / (precision + recall)

def evaluate(model_fn, data):
    """Run a model on dataset and compute metrics."""
    preds = [model_fn(text) for text in data["text"]]

    acc = simple_evaluation(preds, data["label"])
    scores = [entity_level_score(p, r) for p, r in zip(preds, data["label"])]

    return acc, sum(scores) / len(scores)

def run_benchmark():
    data = pd.read_json("data/dataset.json")

    # Debug examples
    print("\n--- SAMPLE OUTPUT (spaCy) ---")
    for text in data["text"][10:12]:
        print("TEXT:", text)
        print("SPACY:", anonymize_spacy(text))
        print()

    print("\n--- SAMPLE OUTPUT (Transformer) ---")
    for text in data["text"][10:12]:
        print("TEXT:", text)
        print("TRANSFORMER:", anonymize_transformer(text))
        print()

    # Evaluation
    print("\n--- BENCHMARK ---")
    for name, fn in {
        "spaCy": anonymize_spacy,
        "Transformer": anonymize_transformer,
    }.items():
        acc, score = evaluate(fn, data)
        print(f"{name} Accuracy: {acc:.2f}")
        print(f"{name} Entity Score: {score:.2f}")

if __name__ == "__main__":
    run_benchmark()