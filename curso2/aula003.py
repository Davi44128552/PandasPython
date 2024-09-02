import numpy as np
import pandas as pd

url = 'docs\\json\\dados_pessoas.json'
dados = pd.read_json(url)
print('\033[1;33m========== INFO INICIAL ==========\033[m')
print(dados.info())
print()

# Convertendo tipos de dados
    # Colocando tudo em object
colunas = dados.columns
dados = dados[colunas].astype(np.object_)
print('\033[1;33m========== INFO OBJECT ==========\033[m')
print(dados.info())
print()

    # Editando cada um
print('\033[1;33m========== COLUNAS ==========\033[m')
print(colunas)
print()

dados['id'] = dados['id'].astype(np.int32)
dados['peso'] = dados['peso'].astype(np.float64)
dados['altura'] = dados['altura'].astype(np.float64)
print('\033[1;33m========== INFO NOVA ==========\033[m')
print(dados.info())