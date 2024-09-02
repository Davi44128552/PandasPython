import pandas as pd

url = 'docs\dados_pessoas.csv'
dados = pd.read_csv(url, sep = ',')

condicao1 = dados['sexo'] == 'F'
condicao2 = dados['altura'] > 1.9
dados_mulheres = dados[(condicao1) & (condicao2)]
n_mulheres = dados_mulheres.shape[0]
print(n_mulheres)