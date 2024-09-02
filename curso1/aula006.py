import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep = ';')

# Aprendendo a tratar valores nulos
    # Tabela com valores nulos(ou não)
print(dados.isnull())

    # Contando número de dados nulos
print(dados.isnull().sum())

    # Tratando
dados = dados.fillna(0)
print(dados)

    # Checando os valores nulos
print(dados.isnull().sum())