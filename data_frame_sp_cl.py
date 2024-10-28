import pandas as pd
import numpy as np

df = pd.read_csv('StudentsPerformance.csv') #Importa o arquivo e armazena dentro de df

print("\n informa as linhas e colunas \n", df.shape)

print("\n Indica um array informando as colunas \n \n", df.columns)
