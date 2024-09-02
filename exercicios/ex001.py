import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep = ';')

print(dados)

# Info da tabela
print('A dimensão da tabela é:', dados.shape)

print("informações sobre as tabelas")
print(dados.columns)
print(dados.info())

# Características de algumas colunas
print(dados['Tipo'].head(5))
print(dados['Tipo'].tail(5))