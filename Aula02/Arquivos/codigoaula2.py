import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

from sklearn.model_selection import train_test_split

# ----------------------------------------------------------
# 1) CARREGAR O DATASET
# ----------------------------------------------------------
df = pd.read_csv("exemplo_dataset2.csv")  # Ajuste para o caminho correto

# Tratar valores ausentes na coluna feedback, se houver
df['feedback'] = df['feedback'].fillna("Desconhecido")

# ----------------------------------------------------------
# 2) CRIAR COLUNA "feedback_Bom" (1 = Bom, 0 = caso contrário)
# ----------------------------------------------------------
df['feedback_Bom'] = (df['feedback'] == 'Bom').astype(int)

# ----------------------------------------------------------
# 3) TRATAR AUSÊNCIAS NUMÉRICAS SIMPLES
#    (idade, renda, nota) - Preencher para evitar problemas
# ----------------------------------------------------------
df['idade'] = df['idade'].fillna(df['idade'].median())
df['renda'] = df['renda'].fillna(df['renda'].mean())
df['nota']  = df['nota'].fillna(df['nota'].median())

# ----------------------------------------------------------
# 4) SEPARAR FEATURES E TARGET, DEPOIS DIVIDIR TREINO/TESTE
# ----------------------------------------------------------
# Usar apenas as colunas numéricas "idade", "renda", "nota" como features
# Se quiser incluir 'cidade' ou 'categoria', a aula não exige codificação extra.
features = df[['idade', 'renda', 'nota']]
target   = df['feedback_Bom']

# Dividir em treino (70%) e teste (30%)
X_train, X_test, y_train, y_test = train_test_split(features, target,
                                                    test_size=0.3,
                                                    random_state=42)

# Converter DataFrames/Series em tensores PyTorch (float32)
X_train_t = torch.tensor(X_train.values, dtype=torch.float32)
y_train_t = torch.tensor(y_train.values, dtype=torch.float32).view(-1, 1)

X_test_t = torch.tensor(X_test.values, dtype=torch.float32)
y_test_t = torch.tensor(y_test.values, dtype=torch.float32).view(-1, 1)

# ----------------------------------------------------------
# 5) DEFINIR REDE NEURAL SIMPLES (BÁSICO)
# ----------------------------------------------------------
class SimpleNet(nn.Module):
    def __init__(self, input_dim):
        super(SimpleNet, self).__init__()
        self.linear1 = nn.Linear(input_dim, 8)  # Camada oculta com 8 neurônios
        self.relu    = nn.ReLU()               
        self.linear2 = nn.Linear(8, 1)         # Saída (1 neurônio p/ binário)

    def forward(self, x):
        x = self.linear1(x)
        x = self.relu(x)
        x = self.linear2(x)
        return x  # logits (não passamos por sigmoid aqui)

input_dim = X_train_t.shape[1]  # Quantidade de colunas em X
model = SimpleNet(input_dim)

# ----------------------------------------------------------
# 6) DEFINIR FUNÇÃO DE PERDA E OTIMIZADOR
# ----------------------------------------------------------
# BCEWithLogitsLoss -> adequado p/ binário (une sigmoid + BCE)
criterion = nn.BCEWithLogitsLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# ----------------------------------------------------------
# 7) LOOP DE TREINAMENTO
# ----------------------------------------------------------
epochs = 10
for epoch in range(epochs):
    # forward
    outputs = model(X_train_t)
    loss = criterion(outputs, y_train_t)
    
    # backward
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    # imprimir estatísticas
    if (epoch+1) % 2 == 0:
        print(f"Época [{epoch+1}/{epochs}], Perda Treino: {loss.item():.4f}")

# ----------------------------------------------------------
# 8) AVALIAR NO CONJUNTO DE TESTE
# ----------------------------------------------------------
with torch.no_grad():
    logits_test = model(X_test_t)
    # Transformar logits em probabilidades [0..1]
    probs_test = torch.sigmoid(logits_test)
    # prob > 0.5 => classe = 1 (Bom)
    preds_test = (probs_test > 0.5).float()

    acertos = (preds_test == y_test_t).sum().item()
    total = y_test_t.shape[0]
    acuracia_test = acertos / total * 100.0

print(f"Acurácia no teste: {acuracia_test:.2f}%")
