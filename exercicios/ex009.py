import pandas as pd

url = 'docs\dados_pessoas.csv'
dados = pd.read_csv(url, sep = ',')
dados.drop('id', axis = 1, inplace = True)

dados.query('sexo == "F" & nacionalidade != "Brasil"', inplace = True)
menor_peso = dados[['peso']].min()
print(menor_peso)