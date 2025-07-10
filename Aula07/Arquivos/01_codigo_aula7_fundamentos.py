# Código referente ao Momento 2: Fundamentos de Redes Neurais
import numpy as np

def neuron_output(inputs, weights, bias, activation='relu'):
    """
    Simula um único neurônio:
      - inputs: array np (features de entrada)
      - weights: array np (pesos)
      - bias: valor escalar
      - activation: 'relu' ou 'sigmoid' (demonstrativo)
    """
    # Soma ponderada
    z = np.dot(inputs, weights) + bias
    
    # Aplica função de ativação
    if activation == 'relu':
        return max(0, z)
    elif activation == 'sigmoid':
        return 1.0 / (1.0 + np.exp(-z))
    else:
        # Se não reconhece a ativação, retorna z sem ativação
        return z

# Exemplo de uso:
inputs = np.array([0.5, -0.2, 1.0])   # 3 entradas
weights = np.array([0.8, -0.5, 0.1]) # 3 pesos correspondentes
bias = 0.2

out_relu = neuron_output(inputs, weights, bias, 'relu')
out_sigmoid = neuron_output(inputs, weights, bias, 'sigmoid')

print("=== Momento 2: Fundamentos de Redes Neurais ===")
print("Inputs :", inputs)
print("Weights:", weights)
print("Bias   :", bias)
print("Saída (ReLU)   :", out_relu)
print("Saída (Sigmoid):", out_sigmoid)
