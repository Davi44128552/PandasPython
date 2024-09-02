import pandas as pd

# Pegando a base de dados
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep = ';') # A função seguinte lê arquivos csv / Especificar o separador(padrão = ',')

# Consultando os dados
print("\033[1;36m========== TODOS OS N TERMOS ==========\033[m")
print(dados) 

print("\033[1;36m========== PRIMEIROS N TERMOS ==========\033[m")
print(dados.head(8)) # Mostrando os n primeiros registros do banco de dados (padrão = 5)

print("\033[1;36m========== ÚLTIMOS N TERMOS ============\033[m")
print(dados.tail(8)) # Mostrando os n últimos registros do banco de dados (padrão = 5)

# Analisando o tipo da tabela
print("\033[1;36m================= TIPO =================\033[m")
print(f'\033[1;33m{type(dados)}\033[m')