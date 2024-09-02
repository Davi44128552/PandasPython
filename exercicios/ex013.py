import pandas as pd

url = 'docs\dados_mercado.csv'
dados = pd.read_csv(url, sep = ',')

# c) Altere o valor do desconto (para zero) de todos os registros onde este campo é nulo.
print(dados.fillna(0, inplace = True))
print(dados)

# Gerando o csv
dados.to_csv('docs\ex013.csv', index = False, sep = ',')
