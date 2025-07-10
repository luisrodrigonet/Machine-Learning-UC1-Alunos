from fbprophet import Prophet
import pandas as pd

# Carregar o dataset
df = pd.read_csv('cotacao_dolar_20250405_103000.csv')

# Treinar o modelo
modelo = Prophet()
modelo.add_country_holidays(country_name='BR')  # Adicionar feriados brasileiros (opcional)
modelo.fit(df)

# Fazer previsão para os próximos 30 dias
futuro = modelo.make_future_dataframe(periods=30)
previsao = modelo.predict(futuro)

# Mostrar resultados
print(previsao[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

# Plotar gráfico
fig = modelo.plot_components(previsao)
