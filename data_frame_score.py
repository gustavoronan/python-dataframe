import pandas as pd
import numpy as np

df = pd.read_csv('StudentsPerformance.csv')

provas = ['math score', 'reading score', 'writing score'] #estamos passando para dentro de provas basicamente os pontos de cada materia
print("\n Função que retorna uma lista da menor para a maior nota dentro da materia de matematica \n", df.sort_values(['math score']))


print("\n \n \n \n \n ")

print("\n Função que retorna uma lista da menor para a maior nota dentro da materia de leitura \n", df.sort_values(['reading score']))


print("\n Função que reseta os index e posteriormente apaga a coluna index \n", df.sort_values(['math score']) .reset_index(drop=True))
