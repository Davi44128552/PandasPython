import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep = ';')

# Criando colunas categóricas
dados.fillna(0, inplace = True)
dados['Possui_suite'] = dados['Suites'].apply(lambda x:'Sim' if x > 0 else 'Não') # Criando condição / apply: aplicar função
print(dados.head())

# Salvando o arquivo
dados.to_csv('dados_completos.csv', index = False, sep = ';')
