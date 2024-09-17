import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

x = sp.Symbol('x')

funciones = [
    sp.sin(x),
    sp.cos(x),
    sp.exp(x),
    sp.log(1 + x),
    1 / (1 - x)
]

funciones_nombres = [
    "sin(x)",
    "cos(x)",
    "exp(x)",
    "log(1 + x)",
    "1 / (1 - x)"
]

def taylor_expansion(funcion, n, a):
    taylor_poly = 0
    for i in range(n + 1):
        term = (sp.diff(funcion, x, i).subs(x, a) * (x - a)**i) / sp.factorial(i)
        taylor_poly += term
    return taylor_poly

def plot_taylor():
    opcion = funciones_nombres.index(combo_funcion.get())
    opcion_funcion = funciones[opcion]
    a = float(entry_a.get())
    n = int(entry_n.get())
    
    x_values = np.linspace(-1, 5, 100)
    taylor_poly_expr = taylor_expansion(opcion_funcion, n, a)
    taylor_poly_lambdified = sp.lambdify(x, taylor_poly_expr, 'numpy')
    p = taylor_poly_lambdified(x_values)
    
    fig, ax = plt.subplots()
    ax.plot(x_values, p, "c--", label="Taylor Polynomial")
    ax.legend()
    ax.set_title(f'Taylor Polynomial of {funciones_nombres[opcion]}')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid()
    
    if opcion == 0:
        ax.set_ylim([-1.5, 1.5])
        ax.plot(x_values, np.sin(x_values), "r--", label="sin(x)")
    elif opcion == 1:
        ax.set_ylim([-1.5, 1.5])
        ax.plot(x_values, np.cos(x_values), "r--", label="cos(x)")
    elif opcion == 2:
        ax.set_ylim([0, np.exp(5)])
        ax.plot(x_values, np.exp(x_values), "r--", label="exp(x)")
    elif opcion == 3:
        ax.set_ylim([-2, 2])
        ax.plot(x_values, np.log(1 + x_values), "r--", label="log(1 + x)")
    elif opcion == 4:
        ax.set_ylim([-10, 10])
        ax.plot(x_values, 1 / (1 - x_values), "r--", label="1 / (1 - x)")
    ax.legend()
    
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=4, column=0, columnspan=2)

window = tk.Tk()
window.title("Taylor Series Plotter")

frame = ttk.Frame(window, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Función:").grid(row=0, column=0, sticky=tk.W)
combo_funcion = ttk.Combobox(frame, values=funciones_nombres)
combo_funcion.grid(row=0, column=1, sticky=(tk.W, tk.E))
combo_funcion.current(0)

ttk.Label(frame, text="Punto de expansión (a):").grid(row=1, column=0, sticky=tk.W)
entry_a = ttk.Entry(frame)
entry_a.grid(row=1, column=1, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Número de términos (n):").grid(row=2, column=0, sticky=tk.W)
entry_n = ttk.Entry(frame)
entry_n.grid(row=2, column=1, sticky=(tk.W, tk.E))

ttk.Button(frame, text="Graficar", command=plot_taylor).grid(row=3, column=0, columnspan=2)

window.mainloop()