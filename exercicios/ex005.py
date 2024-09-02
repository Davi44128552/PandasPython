import pandas as pd

url = 'docs\dados_pessoas.csv'
dados = pd.read_csv(url, sep = ',')
dados.drop('id', axis = 1, inplace = True)

dados_mulheresBr = dados.query('sexo == "F" & nacionalidade == "Brasil"')
dados_mulheresBr = dados_mulheresBr[dados_mulheresBr['nome'].str.startswith('J')] # Startswith
print(dados_mulheresBr)
