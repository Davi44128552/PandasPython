import pandas as pd

url = 'docs\dados_pessoas.csv'
dados = pd.read_csv(url)
dados.drop('id', axis = 1, inplace = True)
print(dados)

dados_homens = dados.query('sexo == "M" & nacionalidade != "Brasil"')
condicao = dados_homens['peso'] < 100
condicao2 = dados_homens['nome'].str.contains('Silva')
dados_homens = dados_homens[(condicao) & (condicao2)]
print(dados_homens)