import numpy as np
from scipy.sparse import coo_matrix
import tkinter as tk
from tkinter import ttk

def convert_to_coo():
    matriz = np.array([
        [int(entry_00.get()), int(entry_01.get()), int(entry_02.get()), int(entry_03.get())],
        [int(entry_10.get()), int(entry_11.get()), int(entry_12.get()), int(entry_13.get())],
        [int(entry_20.get()), int(entry_21.get()), int(entry_22.get()), int(entry_23.get())],
        [int(entry_30.get()), int(entry_31.get()), int(entry_32.get()), int(entry_33.get())]
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

    row, col = np.nonzero(matriz)
    data = matriz[row, col]
    matrix_coo = coo_matrix((data, (row, col)), shape=matriz.shape)
    
    coo_str = "\n".join([f"({i}, {j})\t{v}" for i, j, v in zip(matrix_coo.row, matrix_coo.col, matrix_coo.data)])
    
    result_text.set(f"NZ: {non_zeros}\nIF: {indice_i}\nIC: {indice_j}\n\nMatriz en formato COO:\n{coo_str}")

window = tk.Tk()
window.title("COO Format Converter")

frame = ttk.Frame(window, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Matriz (4x4):").grid(row=0, column=0, columnspan=4)

entry_00 = ttk.Entry(frame, width=5)
entry_00.grid(row=1, column=0)
entry_01 = ttk.Entry(frame, width=5)
entry_01.grid(row=1, column=1)
entry_02 = ttk.Entry(frame, width=5)
entry_02.grid(row=1, column=2)
entry_03 = ttk.Entry(frame, width=5)
entry_03.grid(row=1, column=3)

entry_10 = ttk.Entry(frame, width=5)
entry_10.grid(row=2, column=0)
entry_11 = ttk.Entry(frame, width=5)
entry_11.grid(row=2, column=1)
entry_12 = ttk.Entry(frame, width=5)
entry_12.grid(row=2, column=2)
entry_13 = ttk.Entry(frame, width=5)
entry_13.grid(row=2, column=3)

entry_20 = ttk.Entry(frame, width=5)
entry_20.grid(row=3, column=0)
entry_21 = ttk.Entry(frame, width=5)
entry_21.grid(row=3, column=1)
entry_22 = ttk.Entry(frame, width=5)
entry_22.grid(row=3, column=2)
entry_23 = ttk.Entry(frame, width=5)
entry_23.grid(row=3, column=3)

entry_30 = ttk.Entry(frame, width=5)
entry_30.grid(row=4, column=0)
entry_31 = ttk.Entry(frame, width=5)
entry_31.grid(row=4, column=1)
entry_32 = ttk.Entry(frame, width=5)
entry_32.grid(row=4, column=2)
entry_33 = ttk.Entry(frame, width=5)
entry_33.grid(row=4, column=3)

ttk.Button(frame, text="Convertir a COO", command=convert_to_coo).grid(row=5, column=0, columnspan=4)

result_text = tk.StringVar()
ttk.Label(frame, textvariable=result_text).grid(row=6, column=0, columnspan=4)

window.mainloop()