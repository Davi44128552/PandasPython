import pandas as pd

# Lendo a base de dados
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep = ';')

# Revisando alguns conceitos
dados = dados.query('Tipo == "Apartamento"')
dados = dados.fillna(0)

registros_a_remover = dados.query('Valor == 0 | Condominio == 0').index
dados.drop(registros_a_remover, axis = 0, inplace = True)
dados.drop('Tipo', axis = 1, inplace = True)

# Respondendo algumas questões
    # Apartamentos com 1 quarto e valor < 1200
print("\033[1;35m==================== Aps com 1 quarto e valor < 1200 ====================\033[m")
        # Método 1
print("\033[1;36m==================== Método 1 ====================\033[m")
selecao_final1 = dados.query('Quartos == 1 & Valor < 1200')
print(selecao_final1)

        # Método 2
print("\033[1;36m==================== Método 2 ====================\033[m")
selecao1 = dados['Quartos'] == 1
selecao2 = dados['Valor'] < 1200
selecao_final2 = dados[(selecao1) & (selecao2)]
print(selecao_final2)

    # Apartamentos com 2 quartos, aluguel < 3000 e área > 70
print("\033[1;35m==================== Aps com 2 quartos, valor < 3000 e area > 70 ====================\033[m")
        # Método 1
print("\033[1;36m==================== Método 1 ====================\033[m")
selecao_final3 = dados.query('Quartos == 2 & Valor < 3000 & Area > 70')
print(selecao_final3)

        # Método 2
print("\033[1;36m==================== Método 2 ====================\033[m")
selecao3 = dados['Quartos'] == 2
selecao4 = dados['Valor'] < 3000
selecao5 = dados['Area'] > 70
selecao_final4 = dados[(selecao3) & (selecao4) & (selecao5)]
print(selecao_final4)