import streamlit as st
from src.anonymizer import anonymize_spacy

st.title("🔐 NLP Sensitive Data Anonymizer")

text = st.text_area("Enter text to anonymize:")

if st.button("Anonymize"):
    result = anonymize_spacy(text)
    st.subheader("Anonymized Text")
    st.write(result)