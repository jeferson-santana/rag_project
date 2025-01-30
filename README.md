# RAG Hotmart - Assistente de Respostas com Recuperação e Geração

Este projeto implementa um **sistema de Recuperação Aumentada por Geração (RAG)** para responder perguntas sobre a FAQ da **Hotmart**. Ele combina **busca semântica com FAISS** e **geração de respostas com um modelo FLAN-T5**.

##  **Funcionalidades**
-  **Busca semântica**: Usa embeddings e **FAISS** para encontrar a resposta mais relevante na base da FAQ.
-  **Geração de resposta**: Se não encontrar uma resposta adequada, usa **FLAN-T5** para gerar um texto baseado no contexto.
-  **Processamento eficiente**: Emprega otimizações para acelerar a busca e a geração.

---

##  **Instalação e Execução**
###  **1. Clonar o repositório**
```bash
git clone https://github.com/jeferson-santana/rag_project
cd rag-hotmart
```

###  **2. Criar e ativar um ambiente virtual**
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate      # Windows
```

###  **3. Instalar as dependências**
```bash
pip install -r requirements.txt
```

###  **4. Adicionar o arquivo de dados**
Coloque o arquivo **ProcessoSeletivo[RAG].xlsx** na pasta do projeto.

###  **5. Executar**
Após instalar as dependências e configurar os arquivos, execute:
```bash
python main.py
```

O sistema perguntará:
```bash
Digite uma pergunta sobre a FAQ do Hotmart (ou digite 'sair' para encerrar):
```
Exemplo de resposta:
```
================================================================================
🔹 Pergunta: Como posso modificar o método de pagamento da minha assinatura?
🎯 Resposta: Você pode alterar o método de pagamento acessando...
================================================================================
```

---

##  **Estrutura do Projeto**
```
rag-hotmart/
│── data_loader.py   # Carregamento e tratamento inicial dos dados
│── preprocess.py    # Limpeza e preparação dos textos
│── retriever.py     # Implementação da busca semântica com FAISS
│── generator.py     # Geração de resposta usando FLAN-T5
│── utils.py         # Funções auxiliares
│── config.py        # Definição de parâmetros globais
│── main.py          # Script principal para interação com o usuário
│── requirements.txt # Lista de pacotes necessários
│── README.md        # Documentação do projeto
└── data/            # Pasta onde o arquivo de FAQ deve ser colocado
```

---

##  **Configuração**
O arquivo `config.py` contém os parâmetros ajustáveis, como:
```python
TOP_K = 5  # Número de respostas similares a recuperar
SIMILARITY_THRESHOLD = 0.6  # Limiar de similaridade para considerar resposta válida
```

---

##  **Possíveis Melhorias**
🔹 Implementação de cache de resultados para acelerar buscas repetidas.  
🔹 Afinamento do modelo FLAN-T5 para melhorar a geração de respostas.  
🔹 Desenvolvimento de uma interface web para facilitar a interação com o sistema.  

---