import pandas as pd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep = ';')

imoveis_comerciais = ['Conjunto Comercial/Sala',
                       'Prédio Inteiro', 'Loja/Salão',
                       'Galpão/Depósito/Armazém',
                       'Casa Comercial', 'Terreno Padrão',
                       'Loja Shopping/ Ct Comercial',
                       'Box/Garagem', 'Chácara',
                       'Loteamento/Condomínio', 'Sítio',
                       'Pousada/Chalé', 'Hotel', 'Indústria']

print("\033[1;36m========== Tipos de Registros das tabelas ==========\033[m")
df = dados.query('@imoveis_comerciais not in Tipo')
print(df.Tipo.unique())

# Contando a quantidade de termos por tipo
print("\033[1;36m========== Contador de registros com o tipo ==========\033[m")
print(df.Tipo.value_counts())

# Contando a quantidade de termos de forma fracionária
print("\033[1;36m========== Contador de registros com o tipo (em fração) ==========\033[m")
print(df.Tipo.value_counts(normalize = True)) # Normalize fará a análise fracionária

# Transformando em dataframe
print(df.Tipo.value_counts(normalize = True).to_frame())

# Ordenando em crescente
print(df.Tipo.value_counts(normalize = True).sort_values())

# Criando o gráfico
df_grafico = df.Tipo.value_counts(normalize = True).sort_values()
df_grafico.plot(kind = 'bar', figsize = (10, 8), color = 'green', xlabel = 'Tipo', ylabel = 'Proporção')
plt.show()

# Selecionando apenas os apartamentos
df = df.query('Tipo == "Apartamento"')
print(df.head())