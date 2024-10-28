import pandas as pd
import numpy as np

df = pd.read_csv('StudentsPerformance.csv')

print("\n Gera uma lista com a quantidade de cada genero \n", df.gender.value_counts())
