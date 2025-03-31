import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from algorithms.config import config 
from algorithms.genetic import run_genetic_algorithm



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
        self.root.geometry("300x375")

        self.selection_methods = ["Best", "Roulette", "Tournament"]
        self.cross_methods = ["One-point", "Two-point", "Uniform"]
        self.mutation_methods = ["One-point", "Two-point", "Edge"]

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

        rowEpoch = tk.Frame(main_column)
        rowEpoch.pack(fill="x")
        tk.Label(rowEpoch, text="Epochs").pack(side="left")
        self.epochs_entry = tk.Entry(rowEpoch, width=10)
        self.epochs_entry.pack(side="left")

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

        self.start_button = tk.Button(main_column, text="Start", command=self.run_algorithm)
        self.start_button.pack(fill="x")

    
    def save_results_to_file(self, results):
        """Zapisuje wyniki do pliku tekstowego."""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(results)
                print(f"Wyniki zapisano w: {file_path}")
            except Exception as e:
                print(f"Błąd podczas zapisu: {str(e)}")

    def run_algorithm(self):
        try:
            from algorithms.config import config
            
            config.range_start = float(self.range_start_entry.get())
            config.range_end = float(self.range_end_entry.get())
            config.epochs = int(self.epochs_entry.get())
            config.population_size = int(self.population_amount_entry.get())
            config.precision = int(self.precision_entry.get())
            config.num_variables = int(self.variables_num_entry.get())
            config.selection_method = self.select_method_var.get().lower()
            config.best_selection_amount = int(self.best_amount_entry.get())
            config.tournament_size = int(self.selection_size_entry.get())
            config.crossover_method = self.cross_method_var.get().replace("-", "_").lower()
            config.crossover_probability = float(self.cross_propability_entry.get())
            config.mutation_method = self.mutation_method_var.get().lower()
            config.mutation_probability = float(self.mutation_propability_entry.get())
            config.inversion_probability = float(self.inversion_propability_entry.get())
            config.optimization_type = "max" if self.maximization_var.get() else "min"
            
            best_solution, execution_time = run_genetic_algorithm()
            
            results = f"Najlepsze rozwiązanie: {best_solution.chromosome_value}\nWartość funkcji celu: {best_solution.fitness}\nCzas wykonania: {execution_time} sekund\n"
            
            self.save_results_to_file(results)
        except Exception as e:
            print(f"Błąd: {str(e)}")