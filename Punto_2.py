import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

x = sp.Symbol('x')

funciones = [
    sp.sin(x),
    sp.cos(x),
    sp.exp(x),
    sp.log(1 + x),
    1 / (1 - x)
]

print("Escoge una opción (del 1 al 5)")
print("1. sin(x)")
print("2. cos(x)")
print("3. exp(x)")
print("4. log(1 + x)")
print("5. 1 / (1 - x)")

opcion = int(input()) - 1
opcion_funcion = funciones[opcion]

a = float(input("Ingresa el punto de expansión (a): "))
n = int(input("Ingresa el número de términos (n): "))

x_values = np.linspace(-1, 5, 100)

def taylor_expansion(funcion, n, a):
    taylor_poly = 0
    for i in range(n + 1):
        term = (sp.diff(funcion, x, i).subs(x, a) * (x - a)**i) / sp.factorial(i)
        taylor_poly += term
    return taylor_poly

taylor_poly_expr = taylor_expansion(opcion_funcion, n, a)
taylor_poly_lambdified = sp.lambdify(x, taylor_poly_expr, 'numpy')
p = taylor_poly_lambdified(x_values)

plt.plot(x_values, p, "c--", label="Taylor Polynomial")
plt.legend()
plt.title(f'Taylor Polynomial of {["sin(x)", "cos(x)", "exp(x)", "log(1 + x)", "1 / (1 - x)"][opcion]}')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()


if opcion == 0:
    plt.ylim([-1.5, 1.5])
    plt.plot(x_values, np.sin(x_values), "r--", label="sin(x)")
    plt.legend()
elif opcion == 1:
    plt.ylim([-1.5, 1.5])
    plt.plot(x_values, np.cos(x_values), "r--", label="cos(x)")
    plt.legend()
elif opcion == 2:
    plt.ylim([0, np.exp(5)])
    plt.plot(x_values, np.exp(x_values), "r--", label="exp(x)")
    plt.legend()
elif opcion == 3:
    plt.ylim([-2, 2])
    plt.plot(x_values, np.log(1 + x_values), "r--", label="log(1 + x)")
    plt.legend()
elif opcion == 4:
    plt.ylim([-10, 10])
    plt.plot(x_values, 1 / (1 - x_values), "r--", label="1 / (1 - x)")
    plt.legend()
plt.show()