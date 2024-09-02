import pandas as pd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep = ';')

# Calculando a média do aluguel
media_valor = dados['Valor'].mean()
print("\033[1;35mMédia dos valores: \033[m", media_valor)

# Calculando a média por tipo de imóvel
agrupamento_imoveis = dados.groupby('Tipo')
media_tipo = agrupamento_imoveis[['Valor']].mean().sort_values('Valor')
print(media_tipo)

# Criando um gráfico
media_tipo.plot(kind = 'barh', figsize = (10, 8), color = 'orange')
plt.show()