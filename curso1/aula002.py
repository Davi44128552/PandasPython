import pandas as pd

# Lendo a base de dados
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep = ';')

# Encontrando a dimensão da tabela
print("\033[1;36m========== Dimensões da tabela ========== \033[m ")
print(dados.shape)

# Descrevendo as colunas
print("\033[1;36m========== Informações das colunas ========== \033[m ")
print(dados.columns)

# Obtendo informações adicionais
print("\033[1;36m========== Informações adicionais ========== \033[m ")
print(dados.info())

# Analisando dados específicos das colunas
print("\033[1;36m========== Análise de colunas ========== \033[m")
print("coluna 0: \n", dados['Tipo']) # Object = string

print("coluna 2: \n", dados['Quartos']) # Int64 = int

print("coluna 7: \n", dados['Valor']) # Float64 = float

# Analisando mais de um valor
print(dados[['Tipo', 'Quartos', 'Valor']]) # Necessário estar em forma de matriz