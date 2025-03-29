class Individual:
    def __init__(self, num_variables, bits_per_variable, precision=0, random_init=True):
        """
        Inicjalizacja osobnika z wieloma chromosomami (jeden na zmienną).
        
        Args:
            num_variables: Liczba zmiennych (chromosomów)
            bits_per_variable: Liczba bitów na zmienną
            precision: Precyzja konwersji na wartość rzeczywistą
            random_init: Czy inicjalizować chromosomy losowo
        """
        self.chromosomes = []
        self.fitness = 0
        
        # Inicjalizacja chromosomów (jeden na zmienną)
        for _ in range(num_variables):
            self.chromosomes.append(Chromosome(bits_per_variable, precision, random_init))
    
    def evaluate(self, fitness_func, bounds):
        """
        Oblicz wartość funkcji przystosowania dla osobnika.
        
        Args:
            fitness_func: Funkcja przystosowania
            bounds: Lista krotek (min, max) dla każdej zmiennej
        """
        # Konwersja chromosomów na wartości rzeczywiste
        values = [self.chromosomes[i].to_real_value(bounds[i][0], bounds[i][1]) 
                 for i in range(len(self.chromosomes))]
        
        # Obliczenie przystosowania
        self.fitness = fitness_func(values)
        return self.fitness
    
    def mutate(self, mutation_rate=0.01):
        """Zastosuj mutację do osobnika"""
        for chromosome in self.chromosomes:
            for i in range(chromosome.get_chromosome_len()):
                if random.random() < mutation_rate:
                    chromosome.change_chromosome_bit(i)
