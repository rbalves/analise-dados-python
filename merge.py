import pandas as pd # Para a manipulação de DataFrames
import numpy as np # Cálculo algébricos
import matplotlib.pyplot as plt # Visualização dos dados

norte_brasil_1 = {
    'Siglas': ('AC','AP','AM','PA','RO','RR','TO'),
    'Estados': ('Acre','Amapá', 'Amazonas','Pará','Rondônia','Roraima','Tocantins'),
    'Capitais': ('Rio Branco','Macapá','Manaus','Belém','Porto Velho','Boa Vista','Palmas')
}

df1 = pd.DataFrame(norte_brasil_1)

norte_brasil_2 = {
    'Siglas': ('AC','AP','AM','PA','RO','RR','TO'),
    'Areas':(164123.040, 142828.521, 1559146.876, 1247954.666, 237590.547, 224300.506, 277720.520),
    'População':(869265, 829494, 4080611, 8513497, 1757589, 576568,1555229)
}

df2 = pd.DataFrame(norte_brasil_2)

# Juntando dois dataframes
norte_brasil = pd.merge(df1,df2)

print(norte_brasil)
