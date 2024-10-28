import pandas as pd
import numpy as np

df = pd.read_csv('StudentsPerformance.csv') #Importa o arquivo e armazena dentro de df

print("\n Informações genericas e mais detalhadas \n ",df.info())

print("\n Verifica se existe not a number no DT \n", df.isna().sum())


