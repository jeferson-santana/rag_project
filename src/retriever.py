# retriever.py
import numpy as np
from sentence_transformers import util
from preprocess import clean_text
from config import top_k, similarity_threshold, min_context_threshold, content_similarity_weight, title_similarity_weight, critical_threshold

def search_faq(query, df, embedding_model, index):
    """Busca a melhor resposta no FAQ com base na similaridade semântica"""
    query_embedding = embedding_model.encode([query], normalize_embeddings=True)
    distances, indices = index.search(np.array(query_embedding), k=top_k)

    valid_results = [(idx, dist) for idx, dist in zip(indices[0], distances[0]) if idx != -1]

    if not valid_results:
        return None

    best_match = None
    highest_score = -1

    for idx, dist in valid_results:
        print(f"🔍 Recuperando/Gerando resposta para: '{query}'")
        retrieved_text = df.iloc[idx]["article_content"]
        article_title = df.iloc[idx]["article_name"]

        title_similarity = util.cos_sim(
            embedding_model.encode(query, convert_to_tensor=True),
            embedding_model.encode(article_title, convert_to_tensor=True)
        ).item()

        content_similarity = util.cos_sim(
            embedding_model.encode(query, convert_to_tensor=True),
            embedding_model.encode(retrieved_text, convert_to_tensor=True)
        ).item()

        final_score = (content_similarity_weight * content_similarity) + (title_similarity_weight * title_similarity)

        if final_score > highest_score and final_score > similarity_threshold:
            highest_score = final_score
            best_match = idx

    if highest_score < critical_threshold:
        return "Desculpe, essa pergunta parece estar fora do escopo da Hotmart."

    return clean_text(df.iloc[best_match]["article_content"], query) if best_match is not None else None
