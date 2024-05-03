import pandas as pd

dados = {'Nome':['Pedro', 'Jose'], 'Idade':[22, 35], 'Sexo':['M', 'M'], 'Peso':[64.00, 86.5], 'Altura':[1.83, 1.79]}
df = pd.DataFrame(dados)
print(df)