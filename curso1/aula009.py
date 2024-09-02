import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep = ';')

# Revisando
dados = dados.query('Tipo == "Apartamento"')
dados = dados.fillna(0)
registros_a_remover = dados.query('Valor == 0 | Condominio == 0').index

dados.drop(registros_a_remover, axis = 0, inplace = True)
dados.drop('Tipo', axis = 1, inplace = True)

# Salvando o arquivo em csv
print("\033[1;35m==================== Salvando CSV ====================\033[m")
dados.to_csv('dados_apartamento1.csv')

# Lendo o novo arquivo csv criado
print(pd.read_csv('dados_apartamento1.csv'))

# Removendo o index anterior
print("\033[1;35m==================== Removendo o index anterior ====================\033[m")
dados.to_csv('dados_apartamento2.csv', index = False)
print(pd.read_csv('dados_apartamento2.csv', sep = ','))

# Alterando o separador
print("\033[1;35m==================== Especificando o separador ====================\033[m")
dados.to_csv('dados_apartamento3.csv', index = False, sep = ';')
print(pd.read_csv('dados_apartamento3.csv', sep = ';'))