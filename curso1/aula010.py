# Aula 10: Aprendendo a criar novas colunas
import pandas as pd

# Revisão
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep = ';')
print('\033[1;35m==================== Dez primeiros termos ====================\033[m')
print(dados.head(10))

# Adicionando coluna
print('\033[1;35m==================== Adicionando colunas ====================\033[m')
dados['Valor_por_mes'] = dados['Valor'] + dados['Condominio']
dados['Valor_por_ano'] = (dados['Valor_por_mes'] * 12) + dados['IPTU']

# Printando a base de dados
print('\033[1;35m==================== Colunas novas: ====================\033[m')
print(dados.head())
print(dados.tail())
print(dados.columns)