import pandas as pd
import requests
from datetime import datetime
from prophet import Prophet

# 1. Função para buscar dados históricos da cotação do dólar via API do Banco Central do Brasil
def get_dolar_historico():
    url = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo (dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial='01-01-2023'&@dataFinalCotacao='31-12-2024'&$top=10000&$format=json"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['value']
    else:
        raise Exception("Erro ao acessar a API do Banco Central.")

# 2. Processar os dados
dados = get_dolar_historico()

# Criar DataFrame com as colunas 'data' e 'cotacao'
df = pd.DataFrame(dados)
df['ds'] = df['dataHoraCotacao'].str[:10]  # Extrair apenas a parte da data
df['y'] = df['cotacaoCompra'].astype(float)  # Usar a cotação de compra como valor

# Renomear colunas (opcional)
df = df[['ds', 'y']]

# Converter coluna 'ds' para tipo datetime
df['ds'] = pd.to_datetime(df['ds'])

# Remover duplicatas (manter a última cotação por dia)
df = df.drop_duplicates(subset=['ds'], keep='last')

# Ordenar por data
df = df.sort_values('ds').reset_index(drop=True)

# 3. Salvar como CSV
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"cotacao_dolar_{timestamp}.csv"
df.to_csv(filename, index=False)

print(f"Arquivo '{filename}' criado com sucesso!")
print(f"Amostras dos dados coletados:\n{df.tail()}")