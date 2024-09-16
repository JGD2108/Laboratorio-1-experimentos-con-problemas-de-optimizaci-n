# COO --> Formato de Almacenamiento por Coordenadas
import numpy as np
from scipy.sparse import coo_matrix

"""
NZ: contiene los valores no nulos de la matriz. 
IF: contiene los índices de fila de los elementos no nulos de la matriz.
IC: contiene los índices de columna de los elementos no nulos de la matriz.
"""

matriz = np.array([
    [0, 0, 1, 0],
    [2, 0, 0, 0],
    [0, 0, 3, 0],
    [0, 4, 0, 0]
])

non_zeros = []
indice_i = []
indice_j = []


n_filas = matriz.shape[0]
n_columnas = matriz.shape[1]

for i in range(n_filas):
  for j in range(n_columnas):
    if matriz[i][j] != 0:
      non_zeros.append(int(matriz[i][j]))
      indice_i.append(i)
      indice_j.append(j)
print("")
print("NZ: ", non_zeros)
print("IF: ", indice_i)
print("IC: ", indice_j)


row, col = np.nonzero(matriz)

data = matriz[row, col]

matrix_coo = coo_matrix((data, (row, col)), shape=matriz.shape)

print("Matriz en formato COO:")
print(matrix_coo.toarray())
