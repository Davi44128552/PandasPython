import pandas as pd
import matplotlib.pyplot as plt

url = 'docs\dados_pessoas.csv'
dados = pd.read_csv(url, sep = ',')
dados.drop('id', axis = 1, inplace = True)

dados_programadores = dados.query('sexo == "M" & profissao == "Programador"')
print(dados_programadores)
dados_programadores.to_csv('docs\ex004.csv', index = False, sep = ';')

dados_programadores_peso = dados_programadores.groupby('nome')[['peso']].mean().sort_values('peso')
dados_programadores_peso.plot(kind = 'barh', figsize = (10, 7), color = 'purple')

dados_programadores_altura = dados_programadores.groupby('nome')[['altura']].mean().sort_values('altura')
dados_programadores_altura.plot(kind = 'bar', figsize = (10, 7), color = 'green')

plt.show()