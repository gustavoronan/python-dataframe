import pandas as pd
import numpy as np

df = pd.read_csv('StudentsPerformance.csv') #Importa o arquivo e armazena dentro de df

print("\n Retorna uma estatistica sobre os dados contidos no df \n",df.describe())

print("\n Retorna a quantidade de valores unicos de cada coluna \n", df.nunique())

print("\n Valores unicos de uma coluna especifica \n", df['parental level of education'].unique())

