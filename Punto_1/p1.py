import tkinter as tk
from tkinter import ttk, font, messagebox, simpledialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class FeasibleRegionPlotter:
    def __init__(self, master):
        self.master = master
        self.master.title("Linear Programming Visualizer")
        self.master.geometry("1000x700")
        self.master.configure(bg='#E6E6FA')  # Light lavender background

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TFrame', background='#E6E6FA')
        self.style.configure('TButton', background='#4B0082', foreground='white', font=('Arial', 11, 'bold'), padding=10)
        self.style.map('TButton', background=[('active', '#8A2BE2')])
        self.style.configure('TLabel', background='#E6E6FA', font=('Arial', 12))

        self.a1, self.b1, self.c1 = 2, 3, 40
        self.a2, self.b2, self.c2 = 4, 2, 36

        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self.master, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        title_font = font.Font(family='Arial', size=18, weight='bold')
        title_label = ttk.Label(main_frame, text="Linear Programming Feasible Region Visualizer", font=title_font)
        title_label.pack(pady=(0, 20))

        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=(0, 20))

        buttons = [
            ("Plot Feasible Region", self.plot_feasible_region),
            ("Calculate Cost", self.calculate_cost),
            ("Update Constraints", self.update_constraints)
        ]

        for text, command in buttons:
            btn = ttk.Button(control_frame, text=text, command=command)
            btn.pack(side=tk.LEFT, padx=(0, 10))

        self.plot_frame = ttk.Frame(main_frame)
        self.plot_frame.pack(expand=True, fill=tk.BOTH)

        info_frame = ttk.Frame(main_frame)
        info_frame.pack(fill=tk.X, pady=(20, 0))

        self.info_var = tk.StringVar()
        self.update_info_text()
        info_label = ttk.Label(info_frame, textvariable=self.info_var, justify=tk.LEFT, font=('Arial', 10))
        info_label.pack(side=tk.LEFT)

    def update_info_text(self):
        info_text = f"Constraints:\n{self.a1}x + {self.b1}y ≤ {self.c1}\n{self.a2}x + {self.b2}y ≤ {self.c2}\nx ≥ 0, y ≥ 0"
        self.info_var.set(info_text)

    def plot_feasible_region(self):
        for widget in self.plot_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(figsize=(8, 6), dpi=100)

        x_range = np.linspace(0, 20, 500)
        y_range = np.linspace(0, 25, 500)
        X, Y = np.meshgrid(x_range, y_range)

        inequality1 = self.a1*X + self.b1*Y <= self.c1
        inequality2 = self.a2*X + self.b2*Y <= self.c2
        inequality3 = X >= 0
        inequality4 = Y >= 0

        feasible_region = inequality1 & inequality2 & inequality3 & inequality4
        ax.imshow(feasible_region, extent=[0, 20, 0, 25], origin='lower', cmap='Blues', alpha=0.3)

        ax.plot(x_range, (self.c1 - self.a1*x_range) / self.b1, label=f'{self.a1}x + {self.b1}y = {self.c1}', color='#FF5733', linewidth=2)
        ax.plot(x_range, (self.c2 - self.a2*x_range) / self.b2, label=f'{self.a2}x + {self.b2}y = {self.c2}', color='#33FF57', linewidth=2)

        ax.set_xlabel('x', fontsize=12)
        ax.set_ylabel('y', fontsize=12)
        ax.set_title('Feasible Region', fontsize=16, fontweight='bold')
        ax.set_xlim(0, 20)
        ax.set_ylim(0, 25)
        ax.legend(fontsize=10)
        ax.grid(True, linestyle='--', alpha=0.7)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.set_facecolor('#f8f8f8')
        fig.patch.set_facecolor('#E6E6FA')

        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill=tk.BOTH)

    def calculate_cost(self):
        x = simpledialog.askfloat("Input", "Enter value for x:", parent=self.master)
        y = simpledialog.askfloat("Input", "Enter value for y:", parent=self.master)

        if x is not None and y is not None:
            cost = 5 * x**2 + 8 * y**2
            messagebox.showinfo("Cost Value", f"The cost at point ({x}, {y}) is: {cost:.2f}")

    def update_constraints(self):
        self.a1 = simpledialog.askfloat("Input", f"Enter coefficient a1 (current: {self.a1}):", parent=self.master, initialvalue=self.a1)
        self.b1 = simpledialog.askfloat("Input", f"Enter coefficient b1 (current: {self.b1}):", parent=self.master, initialvalue=self.b1)
        self.c1 = simpledialog.askfloat("Input", f"Enter constant c1 (current: {self.c1}):", parent=self.master, initialvalue=self.c1)

        self.a2 = simpledialog.askfloat("Input", f"Enter coefficient a2 (current: {self.a2}):", parent=self.master, initialvalue=self.a2)
        self.b2 = simpledialog.askfloat("Input", f"Enter coefficient b2 (current: {self.b2}):", parent=self.master, initialvalue=self.b2)
        self.c2 = simpledialog.askfloat("Input", f"Enter constant c2 (current: {self.c2}):", parent=self.master, initialvalue=self.c2)

        self.update_info_text()
        self.plot_feasible_region()

if __name__ == "__main__":
    root = tk.Tk()
    app = FeasibleRegionPlotter(root)
    root.mainloop()