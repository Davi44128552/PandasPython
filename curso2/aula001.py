import pandas as pd

url = 'docs\json\dados_pessoas.json'
dados = pd.read_json(url)
# Existe o método normalize, que organiza o documento json, baseado na coluna que está causando o problema
# pd.json_normalize(base_de_dados['coluna'])

print(dados)