# main.py
from data_loader import load_data, create_embeddings
from retriever import search_faq
from generator import generate_response
from preprocess import clean_response

# Carregar dados e embeddings
df = load_data()
embedding_model, index, df = create_embeddings(df)

while True:
    query = input("\nDigite uma pergunta sobre a FAQ do Hotmart (ou digite 'sair' para encerrar): ").strip()

    if query.lower() == "sair":
        print("\nEncerrando o assistente. Obrigado!\n")
        break

    retrieved_response = search_faq(query, df, embedding_model, index)
    
    if retrieved_response:
        final_response = retrieved_response
    else:
        final_response = generate_response(query, "Infelizmente, não há informações disponíveis no FAQ.")

    print("\n" + "="*80)
    print(f"🔹 Pergunta: {query}")
    print(f"🎯 Resposta: {clean_response(final_response)}")
    print("="*80 + "\n")
