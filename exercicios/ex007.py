import pandas as pd
import matplotlib.pyplot as plt

url = 'docs\dados_pessoas.csv'
dados = pd.read_csv(url)
dados.drop('id', axis = 1, inplace = True)

condicao = dados['sexo'] == 'M'
condicao2 = dados['nacionalidade'] == 'Brasil'
dados_homensBr = dados[(condicao) & (condicao2)]
dhb = dados_homensBr.groupby('nome')[['altura']].mean().sort_values('altura')
print(dhb)
dhb.plot(kind = 'barh', figsize = (9, 7), color = 'green')
plt.show()

maior_valor = dados_homensBr['altura'].max()
print(f'Maior altura: {maior_valor}')