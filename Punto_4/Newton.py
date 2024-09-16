import pandas as pd
from sympy import symbols, diff, ln
import pandas as pd
from tabulate import tabulate
class GeneralizedNewtonMethod:
    def __init__(self, func, x0, max_iter):
        self.func = func
        self.x0 = x0
        self.max_iter = max_iter
        self.x_list = []
        self.fx_list = []
        self.x = symbols('x')
        self.first_derivative = self.first_derivative()
        self.second_derivative = self.second_derivative()

    def first_derivative(self):
        return diff(self.func, self.x)

    def second_derivative(self):
        return diff(self.first_derivative, self.x)
    
    def run(self):
        x = self.x0
        self.x_list.append(x)
        self.fx_list.append(self.func.subs(self.x, x))
        for i in range(self.max_iter):
            x_next = x - (self.first_derivative.subs(self.x, x) / self.second_derivative.subs(self.x, x))
            fx = self.func.subs(self.x, x_next)
            if fx not in self.fx_list:
                self.fx_list.append(fx)
            else:
                break
            self.x_list.append(x_next)
            x = x_next
        df = pd.DataFrame({'x': self.x_list, 'f(x)': self.fx_list})
        return df, i+1
        
        

if __name__ == '__main__':
    headers = ["Experiment", "x_0", "Iterations", "f(x)"]
    x = symbols('x')
    func = 4*x-15*x**2-10
    results=[]

    experiments = [
        {'x0': 0.1, 'max_iter': 5},
        {'x0': 0.5, 'max_iter': 5},
        {'x0': 0.1, 'max_iter': 3},
        {'x0': 0.1, 'max_iter': 8},
    ]

    for idx, exp in enumerate(experiments):
        nm = GeneralizedNewtonMethod(func, exp['x0'], exp['max_iter'])
        result, iterations = nm.run()
        final_fx = result.iloc[-1]['f(x)']
        results.append([f"Start: {exp['x0']}, Iter: {exp['max_iter']}", exp['x0'], iterations, final_fx])
        
    print(tabulate(results, headers=headers, tablefmt="grid"))
        
        
        