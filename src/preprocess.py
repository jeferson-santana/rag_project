# preprocess.py
import re

def clean_text(text, query):
    """Remove caracteres especiais e formatação desnecessária"""
    text = re.sub(r"<[^>]+>", "", text)  # Remove HTML
    text = re.sub(r"\s+", " ", text).strip()  # Remove espaços extras
    text = re.sub(r"={3,}", "", text).strip()  # Remove "====="
    
    query_clean = query.lower().strip("?").strip()
    text_clean = text.lower().strip()
    
    if text_clean.startswith(query_clean):
        text = text[len(query_clean):].strip()
    
    return text

def clean_response(response):
    """Evita repetição da pergunta na resposta final"""
    response = response.strip()
    if "?" in response:
        response = response.split("?", 1)[-1].strip()
    return response
