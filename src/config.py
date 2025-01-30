# config.py

# Número máximo de respostas similares retornadas na busca semântica
top_k = 5  

# Similaridade mínima para considerar uma resposta relevante
similarity_threshold = 0.6  

# Limite mínimo para validar se a resposta está dentro do contexto esperado
min_context_threshold = 0.3  

# Pesos para título e conteúdo
content_similarity_weight = 0.6  
title_similarity_weight = 0.4  

# Definir limiares duplos
critical_threshold = 0.3  
similarity_threshold_faq = 0.55  

# Caminho do arquivo de dados dentro do repositório
file_path = "data/ProcessoSeletivo[RAG].xlsx"
