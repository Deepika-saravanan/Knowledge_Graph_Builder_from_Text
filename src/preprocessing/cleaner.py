import re

def clean_text(text: str) -> str:
    """Basic cleaning"""
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def split_sentences(text: str) -> list:
    """Split text into sentences"""
    sentences = re.split(r"\.|\?|\!", text)
    return [s.strip() for s in sentences if s.strip()]
