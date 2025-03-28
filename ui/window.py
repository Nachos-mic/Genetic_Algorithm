import tkinter as tk
from tkinter import ttk


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

class MainWindow(Singleton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = tk.Tk()
        self.root.title("Genetic Algorithm")
        self.root.geometry("300x350")

        self.selection_methods = ["Roulette", "Tournament", "Random"]
        self.cross_methods = ["Single-point", "Multi-point", "Uniform"]
        self.mutation_methods = ["Random", "Inversion", "Swap"]

        main_column = tk.Frame(self.root)
        main_column.pack(padx=10, pady=10)

        row1 = tk.Frame(main_column)
        row1.pack(fill="x")
        tk.Label(row1, text="Starting Range").pack(side="left")
        self.range_start_entry = tk.Entry(row1, width=10)
        self.range_start_entry.pack(side="left")

        row2 = tk.Frame(main_column)
        row2.pack(fill="x")
        tk.Label(row2, text="Ending Range").pack(side="left")
        self.range_end_entry = tk.Entry(row2, width=10)
        self.range_end_entry.pack(side="left")

        row3 = tk.Frame(main_column)
        row3.pack(fill="x")
        tk.Label(row3, text="Population Amount").pack(side="left")
        self.population_amount_entry = tk.Entry(row3, width=10)
        self.population_amount_entry.pack(side="left")

        row4 = tk.Frame(main_column)
        row4.pack(fill="x")
        tk.Label(row4, text="Precision").pack(side="left")
        self.precision_entry = tk.Entry(row4, width=10)
        self.precision_entry.pack(side="left")

        row5 = tk.Frame(main_column)
        row5.pack(fill="x")
        tk.Label(row5, text="Num of Variables").pack(side="left")
        self.variables_num_entry = tk.Entry(row5, width=10)
        self.variables_num_entry.pack(side="left")

        row6 = tk.Frame(main_column)
        row6.pack(fill="x")
        tk.Label(row6, text="Selection Method").pack(side="left")
        self.select_method_var = tk.StringVar()
        self.select_method_combo = ttk.Combobox(row6, textvariable=self.select_method_var)
        self.select_method_combo['values'] = self.selection_methods
        self.select_method_combo.pack(side="left")

        row7 = tk.Frame(main_column)
        row7.pack(fill="x")
        tk.Label(row7, text="Select best amount").pack(side="left")
        self.best_amount_entry = tk.Entry(row7, width=10)
        self.best_amount_entry.pack(side="left")

        row8 = tk.Frame(main_column)
        row8.pack(fill="x")
        tk.Label(row8, text="Selection size").pack(side="left")
        self.selection_size_entry = tk.Entry(row8, width=10)
        self.selection_size_entry.pack(side="left")

        row9 = tk.Frame(main_column)
        row9.pack(fill="x")
        tk.Label(row9, text="Cross Method").pack(side="left")
        self.cross_method_var = tk.StringVar()
        self.cross_method_combo = ttk.Combobox(row9, textvariable=self.cross_method_var)
        self.cross_method_combo['values'] = self.cross_methods
        self.cross_method_combo.pack(side="left")

        row10 = tk.Frame(main_column)
        row10.pack(fill="x")
        tk.Label(row10, text="Cross Propability").pack(side="left")
        self.cross_propability_entry = tk.Entry(row10, width=10)
        self.cross_propability_entry.pack(side="left")

        row11 = tk.Frame(main_column)
        row11.pack(fill="x")
        tk.Label(row11, text="Mutation Method").pack(side="left")
        self.mutation_method_var = tk.StringVar()
        self.mutation_method_combo = ttk.Combobox(row11, textvariable=self.mutation_method_var)
        self.mutation_method_combo['values'] = self.mutation_methods
        self.mutation_method_combo.pack(side="left")

        row12 = tk.Frame(main_column)
        row12.pack(fill="x")
        tk.Label(row12, text="Mutation Propability").pack(side="left")
        self.mutation_propability_entry = tk.Entry(row12, width=10)
        self.mutation_propability_entry.pack(side="left")

        row13 = tk.Frame(main_column)
        row13.pack(fill="x")
        tk.Label(row13, text="Inversion Probability").pack(side="left")
        self.inversion_propability_entry = tk.Entry(row13, width=10)
        self.inversion_propability_entry.pack(side="left")

        row14 = tk.Frame(main_column)
        row14.pack(fill="x")
        tk.Label(row14, text="Maximization").pack(side="left")
        self.maximization_var = tk.BooleanVar()
        self.maximization_checkbox = tk.Checkbutton(row14, variable=self.maximization_var)
        self.maximization_checkbox.pack(side="left")

        self.start_button = tk.Button(main_column, text="Start")
        self.start_button.pack(fill="x")
