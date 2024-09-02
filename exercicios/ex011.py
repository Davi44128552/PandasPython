import pandas as pd

url = 'docs\dados_mercado.csv'
dados = pd.read_csv(url, sep = ',')

# a) Pesquise os itens que foram vendidos sem desconto. As colunas presentes no
#	 resultado da consulta são: ID_NF, ID_ITEM, COD_PROD E VALOR_UNIT.


condicao = dados['desconto'].isnull()
dados_sem_desconto = dados[(condicao)]
dados_sem_desconto.drop('quantidade', axis = 1, inplace = True)
dados_sem_desconto.drop('desconto', axis = 1, inplace = True)
print(dados_sem_desconto)
dados_sem_desconto.to_csv('docs\ex011.csv', index = False, sep = ',')