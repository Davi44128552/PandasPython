import pandas as pd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep = ';')

print(dados.Tipo.unique())
imoveis_comerciais = ['Conjunto Comercial/Sala',
                       'Prédio Inteiro', 'Loja/Salão',
                       'Galpão/Depósito/Armazém',
                       'Casa Comercial', 'Terreno Padrão',
                       'Loja Shopping/ Ct Comercial',
                       'Box/Garagem', 'Chácara',
                       'Loteamento/Condomínio', 'Sítio',
                       'Pousada/Chalé', 'Hotel', 'Indústria']

dados_imoveis_residenciais = dados.query('@imoveis_comerciais not in Tipo')
df_imoveis_residenciais = dados_imoveis_residenciais.groupby('Tipo')[['Valor']].mean().sort_values('Valor')
print(df_imoveis_residenciais)

# gráfico
df_imoveis_residenciais.plot(kind = 'barh', figsize = (10, 8), color = 'purple')
plt.show()