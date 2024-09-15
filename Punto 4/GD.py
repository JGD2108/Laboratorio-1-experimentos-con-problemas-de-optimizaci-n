import sympy as sp
from tabulate import tabulate
import numpy as np
import matplotlib.pyplot as plt  # Added for plotting

class GradientDescent:
    def __init__(self, func, initial_point: float, learn_rate: float, max_iter: int):
        self.func = func
        self.initial_point = initial_point
        self.learn_rate = learn_rate
        self.max_iter = max_iter
        self.variables = self._get_variables()

    def _get_variables(self):
        return list(self.func.free_symbols)

    def is_differentiable(self):
        try:
            sp.diff(self.func)
            return True
        except:
            return False

    def is_convex(self):
        try:
            expr = sp.sympify(self.func)
            if len(self.variables) == 1:
                x = self.variables[0]
                second_derivative = sp.diff(expr, x, 2)
                result = sp.solve(second_derivative < 0, x, domain=sp.S.Reals)
                return len(result) == 0
            else:
                hessian = sp.hessian(expr, self.variables)
                return self._is_positive_semidefinite(hessian)
        except:
            return False

    def _is_positive_semidefinite(self, matrix):
        n = matrix.shape[0]
        x = sp.symbols(f'x:{n}')
        quad_form = sum(x[i]*x[j]*matrix[i,j] for i in range(n) for j in range(n))
        return sp.solve(quad_form < 0, x, domain=sp.S.Reals) == []

    def check_validity(self):
        variables = self._get_variables()
        diff = self.is_differentiable()
        print(diff)
        if diff:
            self.is_convex()
        else:
            print("Esta función no se puede calcular correctamente usando el método de Gradient Descent")

    def gradient_descent(self, tol: float = 0.01):
        x = self.initial_point
        steps = [self.initial_point]  # history tracking

        gradient = sp.lambdify(self.variables, sp.diff(self.func, self.variables[0]), 'numpy')

        for i in range(self.max_iter):
            diff = self.learn_rate * gradient(x)
            if np.abs(diff) < tol:
                break
            x = x - diff
            steps.append(x)  # history tracing

        return steps, x, i + 1  # Return the number of iterations

    def run_algorithm(self):
        if self.is_differentiable():
            steps, x, iterations = self.gradient_descent()
            return steps, x, iterations
        else:
            return None

    def plot_convergence(self, steps):
        plt.plot(range(len(steps)), steps, marker='o')
        plt.title(f'Convergence Plot (LR: {self.learn_rate})')
        plt.xlabel('Iterations')
        plt.ylabel('x value')
        plt.show()


# Define the function and experiments
x = sp.symbols('x')
func1 = x**2 - 4*x + 1

experiments = [
    [func1, 0, 0.1, 5],
    [func1, 0, 0.1, 5],
    [func1, 0.5, 0.1, 5],
    [func1, 0.1, 0.1, 5],
    [func1, 0.1, 0.1, 15],
    [func1, 0.1, 0.1, 20],
    [func1, 0, 0.5, 10],
    [func1, 0, 0.1, 10],
]

results = []
headers = ["Experiment", "Final x", "Iterations"]

# Run the experiments
for idx, exp in enumerate(experiments):
    gd = GradientDescent(exp[0], exp[1], exp[2], exp[3])
    result = gd.run_algorithm()
    if result:
        steps, final_x, iterations = result
        results.append([f"Start: {exp[1]}, LR: {exp[2]}, Iter: {exp[3]}", final_x, iterations])
        # Plot convergence for each experiment
        gd.plot_convergence(steps)  # Added to show convergence for each run

# Print the results in a table format
print(tabulate(results, headers=headers, tablefmt="grid"))

# Analysis of results
for exp, final_x, iterations in results:
    print(f"{exp}: Final x = {final_x}, Iterations = {iterations}")
