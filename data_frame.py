import pandas as pd
import numpy as np

df = pd.read_csv('StudentsPerformance.csv') #Importa o arquivo e armazena dentro de df

print("\n Visualização das primeiras 5 linhas \n",df.head())

print("\n Visualização das ultimas 5 linhas \n", df.tail())


