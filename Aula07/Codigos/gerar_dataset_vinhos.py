import pandas as pd
import numpy as np

# Gerando dados simulados
np.random.seed(42)
n_samples = 200

data = {
    'acidez': np.round(np.random.uniform(3.0, 8.5, n_samples), 2),
    'teor_alcoolico': np.round(np.random.uniform(8.0, 14.0, n_samples), 2),
    'ph': np.round(np.random.uniform(2.9, 3.6, n_samples), 2),
    'residuo_acucar': np.round(np.random.uniform(1.0, 3.5, n_samples), 2),
    'densidade': np.round(np.random.uniform(0.990, 1.010, n_samples), 3),
    'qualidade': np.random.choice(['bom', 'ruim'], size=n_samples)
}

# Criando DataFrame
df = pd.DataFrame(data)

# Gerando timestamp para o nome do arquivo
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"vinhos_qualidade_{timestamp}.csv"

# Salvando como CSV com timestamp no nome
df.to_csv(filename, index=False)

print(f"Arquivo '{filename}' criado com sucesso!")