import pandas as pd
import matplotlib.pyplot as plt

# Lendo a base de dados
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep = ';')

# Removendo imóveis comerciais
    # Olhando todos os tipos de imoveis
print(dados.Tipo.unique())
imoveis_comerciais = ['Conjunto Comercial/Sala',
                       'Prédio Inteiro', 'Loja/Salão',
                       'Galpão/Depósito/Armazém',
                       'Casa Comercial', 'Terreno Padrão',
                       'Loja Shopping/ Ct Comercial',
                       'Box/Garagem', 'Chácara',
                       'Loteamento/Condomínio', 'Sítio',
                       'Pousada/Chalé', 'Hotel', 'Indústria']

    # Removendo todos os registros de imóveis comerciais
print("\033[1;36m========== Imóveis Comerciais ==========\033[m")
print(dados.query('@imoveis_comerciais in Tipo')) # Seleciona termos da base de dados de acordo com a condição imposta (select/where)

print("\033[1;36m========== Imóveis Residenciais ==========\033[m")
print(dados.query('@imoveis_comerciais not in Tipo'))
df = dados.query('@imoveis_comerciais not in Tipo')
print(df.head())

print("\033[1;36m========== Tipos de imóveis Residenciais ==========\033[m")
print(df.Tipo.unique())
df_grafico = df.groupby('Tipo')[['Valor']].mean().sort_values('Valor')
df_grafico.plot(kind = 'barh', figsize = (7, 5), color = 'green')
plt.show()