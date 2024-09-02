import pandas as pd
import matplotlib.pyplot as plt

# Lendo a base de dados
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep = ';')

# Respondendo algumas perguntas
    # Qual valor médio de aluguel por tipo de imóvel?
print(dados.head())
print("\033[34mDados importantes: 'Tipo' e 'Valor'\033[m")

print("\033[1;36m========== Média dos valores ==========\033[m")
print(dados['Valor'].mean()) # Essa função calcula as médias de algum valor da tabela

    # Agrupando dados
print("\033[1;36m========== Calculando a média dos números agrupados por tipo ==========\033[m")
print(dados.groupby('Tipo').mean(numeric_only = True)) # groupby agrupa / numericonly especifica que são apenas numeros

    # Respondendo a pergunta
print("\033[1;36m========== Calculando a média de valores por tipo de imóvel ==========\033[m")
print(dados.groupby('Tipo')['Valor'].mean()) # Agrupando e calculando média de algo específico

    # Respondendo em dataframe e organizando
print("\033[1;36m========== Organizado ==========\033[m")
print(dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor')) # Sort = ordenar

# Transformando os dados obtidos em gráfico
print("\033[1;36m========== Gráfico ==========\033[m")
dados_agrupado_tv = dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor')
dados_agrupado_tv.plot(kind = 'barh', figsize = (5, 3), color = 'green')
plt.show()