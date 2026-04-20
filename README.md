# NLP Sensitive Data Anonymizer

## Overview
This project extracts and anonymizes sensitive information using pre-trained NER models (spaCy and BERT).

## Installation
pip install -r requirements.txt

## Usage
Run Commands
```bash
python -m src.benchmark
streamlit run app.py
uvicorn src.api:app --reload
```

## Models
- spaCy: en_core_web_sm
- Transformers: dslim/bert-base-NER

## Results
| Model | f1 Entity Score |
|------|----------|
| spaCy | 0.84 |
| BERT | 0.63 |