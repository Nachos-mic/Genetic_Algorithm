import numpy as np

def hypersphere(x) -> float:
    return sum(xi ** 2 for xi in x)

def martin_and_gaddy(chromosome):
    if chromosome.chromosome_value is None:
        print("Ostrzeżenie: chromosome_value jest None")
        return float('inf') 
    
    if len(chromosome.chromosome_value) < 2:
        print("Ostrzeżenie: chromosome_value ma mniej niż 2 elementy")
        return float('inf')
        
    x1, x2 = chromosome.chromosome_value[:2]
    return (x1 - x2) ** 2 + ((x1 + x2 - 10) / 3) ** 2


def evaluate_fitness(chromosome):
    from algorithms.config import config
    if config.function == "Martin and Gaddy":
        return martin_and_gaddy(chromosome)
    elif config.function == "hypersphere":
        return hypersphere(chromosome.chromosome_value)

