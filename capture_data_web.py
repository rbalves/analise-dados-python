import pandas as pd # Para a manipulação de DataFrames
import numpy as np # Cálculo algébricos
import matplotlib.pyplot as plt # Visualização dos dados

#Procura uma tabela na página e retorna em forma de lista
cod_bancos=pd.read_html('https://www.codigobanco.com')

print(cod_bancos[0])
