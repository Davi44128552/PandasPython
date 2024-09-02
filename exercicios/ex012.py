import pandas as pd

url = 'docs\dados_mercado.csv'
dados = pd.read_csv(url, sep = ',')

# b) Pesquise os itens que foram vendidos com desconto. As colunas presentes no
#    resultado da consulta são: ID_NF, ID_ITEM, COD_PROD, VALOR_UNIT E O VALOR
#    VENDIDO. OBS: O valor vendido é igual ao VALOR_UNIT -
#    (VALOR_UNIT*(DESCONTO/100)).

# Aplicando a condição
condicao = dados['desconto'].notnull()
dados_sem_desconto = dados[condicao]

# Adicionando uma nova coluna
operacao = dados_sem_desconto['valor_unit'] - (dados_sem_desconto['valor_unit'] * (dados_sem_desconto['desconto'] / 100))
dados_sem_desconto['valor_vendido'] = operacao

# Removendo colunas
dados_sem_desconto.drop('quantidade', axis = 1, inplace = True)
dados_sem_desconto.drop('desconto', axis = 1, inplace = True)

# Printando o resultado
print(dados_sem_desconto)

# Gerando o arquivo csv
dados_sem_desconto.to_csv('docs\ex012.csv', index = False, sep = ';')