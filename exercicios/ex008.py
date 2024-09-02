import pandas as pd

url = 'docs\dados_pessoas.csv'
dados = pd.read_csv(url, sep = ',')

dados_media = dados[['peso']].mean()
print(dados_media)