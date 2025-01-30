# data_loader.py
import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from config import file_path

def load_data():
    """Carrega os dados do FAQ"""
    print("Carregando dados do FAQ...")
    df = pd.read_excel(file_path)
    print(f"✅ Dados carregados! {df.shape[0]} registros encontrados.\n")
    return df

def create_embeddings(df):
    """Gera embeddings e cria um índice FAISS"""
    print("🔄 Gerando embeddings para os artigos do FAQ...")
    embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    df["embeddings"] = df["article_content"].apply(lambda x: embedding_model.encode(x, normalize_embeddings=True))
    embeddings_matrix = np.array(df["embeddings"].tolist())
    print("✅ Embeddings gerados com sucesso! Iniciando indexação FAISS...\n")

    # Criando índice FAISS
    print("📌 Criando índice FAISS...")
    dimension = embeddings_matrix.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings_matrix)

    print("✅ Índice FAISS criado com sucesso!\n")
    return embedding_model, index, df
