import pandas as pd # Para a manipulação de DataFrames
import numpy as np # Cálculo algébricos
import matplotlib.pyplot as plt # Visualização dos dados

gas = pd.read_csv('glp.csv', sep=';', encoding='latin1')

gas.drop(['Região - Sigla','CNPJ da Revenda', 'Unidade de Medida', 'Bandeira'], axis=1, inplace = True)
gas.drop(['Produto'], axis=1, inplace = True)

#Renomeando as colunas
gas.columns = ['Estado', 'Municipio', 'Revenda', 'Data', 'Venda', 'Compra']

#Buscando dados do Amazonas
gas_am = gas[gas['Estado'] == 'AM']

#Apagando nulos
gas_am = gas_am.dropna(subset=['Compra'])

#Criando coluna lucro
gas_am['Lucro']=gas_am['Venda'] - gas_am['Compra']

#Ordenando pelo valor de venda em ordem crescente
gas_am.sort_values(by='Venda', ascending=True)

#Dados de Manaus
gas_manaus=gas_am[gas_am['Municipio']=='MANAUS'].sort_values(by='Venda')

# Exibe: média, desvio padrão, valor mínimo, valor máximo
print(gas_am.describe())

#Salvando em arquivo
gas_manaus.to_csv("gas_manaus.csv")
