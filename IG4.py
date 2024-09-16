import tkinter as tk
from tkinter import ttk
import sympy as sp
import numpy as np
from Punto_4.Newton import GeneralizedNewtonMethod
from Punto_4.GD import GradientDescent
from Punto_4.GA import GeneticAlgorithm
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class OptimizationGUI:
    def __init__(self, master):
        self.master = master
        master.title("Optimization Methods Comparison")
        master.geometry("1200x550")  # Increased window size
        master.configure(bg='#f0f0f0')  # Light gray background

        self.style = ttk.Style()
        self.style.theme_use('clam')  # Use 'clam' theme for a modern look
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 12))
        self.style.configure('TButton', font=('Arial', 12, 'bold'), background='#4CAF50', foreground='white')
        self.style.configure('TEntry', font=('Arial', 12))
        self.style.configure('TCombobox', font=('Arial', 12))

        self.create_widgets()

    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.master, padding="10 10 10 10", style='TFrame')
        main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(0, weight=1)

        # Function input
        ttk.Label(main_frame, text="Function:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.func_entry = ttk.Entry(main_frame, width=50, font=('Arial', 12))
        self.func_entry.grid(row=0, column=1, columnspan=3, padx=5, pady=5, sticky=(tk.W, tk.E))
        self.func_entry.insert(0, "2*x - ln(x)")

        # Method selection
        ttk.Label(main_frame, text="Method:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.method_var = tk.StringVar()
        methods = ["Newton", "Gradient Descent", "Genetic Algorithm"]
        self.method_combo = ttk.Combobox(main_frame, textvariable=self.method_var, values=methods, font=('Arial', 12))
        self.method_combo.grid(row=1, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
        self.method_combo.bind("<<ComboboxSelected>>", self.update_parameter_fields)

        # Parameter inputs
        self.param_labels = []
        self.param_entries = []
        for i in range(4):
            label = ttk.Label(main_frame, text="")
            label.grid(row=2+i, column=0, padx=5, pady=5, sticky=tk.W)
            entry = ttk.Entry(main_frame, font=('Arial', 12))
            entry.grid(row=2+i, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
            self.param_labels.append(label)
            self.param_entries.append(entry)

        # Run button
        self.run_button = ttk.Button(main_frame, text="Run Optimization", command=self.run_optimization)
        self.run_button.grid(row=6, column=0, columnspan=2, padx=5, pady=20, sticky=(tk.W, tk.E))

        # Results area
        self.results_text = tk.Text(main_frame, height=10, width=60, font=('Arial', 12), bg='#ffffff', fg='#333333')
        self.results_text.grid(row=7, column=0, columnspan=4, padx=5, pady=5, sticky=(tk.W, tk.E))

        # Plot area
        self.fig, self.ax = plt.subplots(figsize=(6, 5))
        self.canvas = FigureCanvasTkAgg(self.fig, master=main_frame)
        self.canvas.get_tk_widget().grid(row=0, column=4, rowspan=8, padx=10, pady=10, sticky=(tk.N, tk.S, tk.E, tk.W))

        # Configure plot style
        plt.style.use('ggplot')
        self.ax.set_facecolor('#f0f0f0')
        self.fig.patch.set_facecolor('#f0f0f0')

    def update_parameter_fields(self, event=None):
        method = self.method_var.get()
        if method == "Newton":
            params = ["x0", "max_iter"]
        elif method == "Gradient Descent":
            params = ["initial_point", "learn_rate", "max_iter"]
        elif method == "Genetic Algorithm":
            params = ["population_size", "num_generations", "mutation_rate"]
        else:
            params = []

        for i, (label, entry) in enumerate(zip(self.param_labels, self.param_entries)):
            if i < len(params):
                label.config(text=params[i])
                entry.config(state="normal")
            else:
                label.config(text="")
                entry.delete(0, tk.END)
                entry.config(state="disabled")

    def run_optimization(self):
        func_str = self.func_entry.get()
        x = sp.symbols('x')
        func = sp.sympify(func_str)

        method = self.method_var.get()
        params = [entry.get() for entry in self.param_entries if entry.get()]

        try:
            if method == "Newton":
                optimizer = GeneralizedNewtonMethod(func, float(params[0]), int(params[1]))
                result, iterations = optimizer.run()
                self.plot_results(result['x'], result['f(x)'])
                self.display_results(f"Newton's Method:\nFinal x: {result['x'].iloc[-1]}\nFinal f(x): {result['f(x)'].iloc[-1]}\nIterations: {iterations}")

            elif method == "Gradient Descent":
                optimizer = GradientDescent(func, float(params[0]), float(params[1]), int(params[2]))
                steps, final_x, iterations = optimizer.run_algorithm()
                self.plot_results(steps, [func.subs(x, step) for step in steps])
                self.display_results(f"Gradient Descent:\nFinal x: {final_x}\nFinal f(x): {func.subs(x, final_x)}\nIterations: {iterations}")

            elif method == "Genetic Algorithm":
                optimizer = GeneticAlgorithm(func, int(params[0]), int(params[1]), float(params[2]))
                best_x, best_fx, generations = optimizer.run()
                self.display_results(f"Genetic Algorithm:\nBest x: {best_x}\nBest f(x): {best_fx}\nGenerations: {generations}")
                self.ax.clear()
                self.ax.set_title('No plot for Genetic Algorithm')
                self.canvas.draw()

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            self.display_results(error_message)
            self.ax.clear()
            self.ax.text(0.5, 0.5, error_message, ha='center', va='center', fontsize=12, color='red')
            self.ax.set_axis_off()
            self.canvas.draw()
    def display_results(self, text):
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, text)

 

    def plot_results(self, x_values, y_values):
        self.ax.clear()
        try:
            # Convert to numpy arrays and get real parts
            x = np.real(np.array(x_values, dtype=complex))
            y = np.real(np.array(y_values, dtype=complex))
            
            self.ax.plot(x, y, '-', color='#1E88E5', linewidth=2, marker='o', markersize=8)
            self.ax.set_xlabel('x', fontsize=12)
            self.ax.set_ylabel('f(x)', fontsize=12)
            self.ax.set_title('Optimization Progress', fontsize=14, fontweight='bold')
            self.ax.grid(True, linestyle='--', alpha=0.7)
        except (TypeError, ValueError) as e:
            self.ax.text(0.5, 0.5, 'Error: Complex values encountered\nCannot plot results',
                        ha='center', va='center', fontsize=12, color='red')
            self.ax.set_axis_off()
        
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = OptimizationGUI(root)
    root.mainloop()