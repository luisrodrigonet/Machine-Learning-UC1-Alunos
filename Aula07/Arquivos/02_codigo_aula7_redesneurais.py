# código referente ao momento 4 de redes neurais
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 1) Gerar ou carregar dados sintéticos para classificação binária
#    Ex.: y=1 se (x1 + x2 > 1.0), caso contrário y=0 (uma lógica simples).
np.random.seed(42)
X_data = np.random.rand(200, 2)  # 200 amostras, 2 features
y_data = (X_data[:,0] + X_data[:,1] > 1.0).astype(int)

# Dividir treino/teste
X_train, X_test, y_train, y_test = train_test_split(
    X_data, y_data, test_size=0.3, random_state=42
)

# Converter a tensores
X_train_t = torch.tensor(X_train, dtype=torch.float32)
y_train_t = torch.tensor(y_train, dtype=torch.float32).view(-1,1)

X_test_t = torch.tensor(X_test, dtype=torch.float32)
y_test_t = torch.tensor(y_test, dtype=torch.float32).view(-1,1)

# 2) Definir a rede neural
class AdvancedNet(nn.Module):
    def __init__(self, input_dim=2):
        super(AdvancedNet, self).__init__()
        self.fc1 = nn.Linear(input_dim, 8)  # Camada oculta 1
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(8, 4)         # Camada oculta 2
        self.fc3 = nn.Linear(4, 1)         # Saída (1 neurônio p/ binário)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        return x  # logits (não passamos por sigmoid)

model = AdvancedNet(input_dim=2)

# 3) Função de perda + otimizador
criterion = nn.BCEWithLogitsLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# 4) Loop de treinamento
epochs = 20
for epoch in range(epochs):
    # forward
    outputs = model(X_train_t)
    loss = criterion(outputs, y_train_t)
    
    # backward
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    if (epoch+1) % 5 == 0:
        print(f"Época {epoch+1}/{epochs}, Perda Treino: {loss.item():.4f}")

# 5) Avaliar no teste
with torch.no_grad():
    logits_test = model(X_test_t)
    probs_test = torch.sigmoid(logits_test)  # Converter logits para [0..1]
    preds_test = (probs_test > 0.5).float()

    # Converter tensores em NumPy para usar accuracy_score
    acc = accuracy_score(y_test_t.numpy(), preds_test.numpy())
    print(f"\nAcurácia no teste: {acc*100:.2f}%")
