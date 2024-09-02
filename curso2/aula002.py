import pandas as pd

url = 'docs\json\dados_pessoas.json'
dados = pd.read_json(url)

# Obtendo as colunas em lista
colunas = list()
colunas = dados.columns
print('\033[1;33m========== COLUNAS ==========\033[m')
print(colunas)
print()

# Separando dados agrupados
# base_de_dados.explode(colunas[intervalo])

# Resetando os índices
dados.reset_index(inplace = True, drop = True)
print(print('\033[1;33m========== DADOS ==========\033[m'))
print(dados)
print()

print('\033[1;33m========== DADOS INFO ==========\033[m')
print(dados.info())