import re
import nltk
import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

# -> Se for a primeira vez usando NLTK:
# nltk.download('stopwords')

# Lista de textos de exemplo
texts = [
    "Olá, tudo bem? Este é um texto de Exemplo!",
    "Eu amo programação em Python e Machine Learning.",
    "Texto com MUITAS PONTUAÇÕES... e alguns STOP WORDS!",
    "Outro exemplo: A corrida de dados é essencial em ML!!!"
]

# 1) Definir stopwords (ex.: português, mas ajuste conforme sua necessidade)
stopwords_pt = set(stopwords.words('portuguese'))  # "de", "a", "o", "e", ...

# 2) Função de limpeza e tokenização
def preprocess_text(text):
    # a) Colocar tudo em minúsculo
    text = text.lower()
    # b) Remover pontuações e caracteres especiais (regex)
    text = re.sub(r'[^a-z0-9\s]', '', text)
    # c) Tokenizar de forma simples (split por espaço)
    tokens = text.split()
    # d) Remover stopwords
    tokens = [t for t in tokens if t not in stopwords_pt]
    # (Opcional: aplicar stemming/lemmatization, dependendo do caso)
    # e) Reunir tokens novamente, se quisermos gerar um "texto limpo"
    return " ".join(tokens)

# 3) Limpar cada texto na lista
cleaned_texts = [preprocess_text(txt) for txt in texts]

# 4) Vetorizar com CountVectorizer (Bag-of-Words)
vectorizer = CountVectorizer()
bow_matrix = vectorizer.fit_transform(cleaned_texts)

# 5) Converter para DataFrame, apenas para visualização
bow_df = pd.DataFrame(bow_matrix.toarray(), columns=vectorizer.get_feature_names_out())

print("Textos originais:")
for i, t in enumerate(texts):
    print(f"{i+1}: {t}")

print("\nTextos pós-limpeza:")
for i, ct in enumerate(cleaned_texts):
    print(f"{i+1}: {ct}")

print("\nMatriz Bag-of-Words:")
print(bow_df)
