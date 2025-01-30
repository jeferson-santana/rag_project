# generator.py
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Carregar modelo de geração de texto
model_name = "google/flan-t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name, legacy=True)
generator_model = T5ForConditionalGeneration.from_pretrained(model_name)

def generate_response(query, retrieved_text):
    """Gera uma resposta usando o modelo T5 baseado no contexto"""
    prompt = f"Baseado no seguinte contexto, responda a pergunta de forma curta e objetiva:\nContexto: {retrieved_text}\nPergunta: {query}\nResposta:"
    
    inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
    output = generator_model.generate(**inputs, max_length=256, num_return_sequences=1)
    print(f"⚡ Gerando resposta via modelo T5 para: '{query}'")
    return tokenizer.decode(output[0], skip_special_tokens=True)
    print(f"✅ Resposta gerada com sucesso!\n")