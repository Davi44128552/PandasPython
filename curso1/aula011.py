import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep = ';')

# Criando colunas categóricas
dados['Descricao'] = dados['Tipo'] + ' em ' + dados['Bairro'] + ' com ' + \
                     dados['Quartos'].astype(str) + ' quartos ' + \
                     ' e ' + dados['Vagas'].astype(str) + ' vaga(s) de estacionamento '

print(dados.head())
print(dados.tail())