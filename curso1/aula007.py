# Aprendendo a remover valores inconsistentes
import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep = ';')

dados = dados.query('Tipo == "Apartamento"')
dados = dados.fillna(0)

# Selecionando os valores 0
print(dados.query('Valor == 0 | Condominio == 0'))

# Retornando todas as index com 0
print(dados.query('Valor == 0 | Condominio == 0').index)
registros_a_remover = dados.query('Valor == 0 | Condominio == 0').index

# Removendo estes valores
dados.drop(registros_a_remover, axis = 0, inplace = True) # axis: 0 = linhas / 1 = colunas
print(dados.head(10))

# Removendo a coluna tipo
dados.drop('Tipo', axis = 1, inplace = True)
print(dados.tail(7))