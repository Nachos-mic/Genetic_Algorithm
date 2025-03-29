import numpy as np

def hypersphere(x) -> float:
    return sum(xi ** 2 for xi in x)

def martin_and_gaddy(x1: float, x2: float) -> float:
    """
    Implementacja funkcji Martin and Gaddy:
    f(x) = (x1 - x2)² + ((x1 + x2 - 10) / 3)²
    """
    return (x1 - x2) ** 2 + ((x1 + x2 - 10) / 3) ** 2

"""
def hypersphere(x):
    return sum(xi ** 2 for xi in x)

def martin_and_gaddy(x):
    return (x[0] - x[1])**2 + ((x[0] + x[1] - 10) / 3)**2

def evaluate_fitness(chromosome):
    if config.function == "hypersphere":
        return hypersphere(chromosome.chromosome_value)
    elif config.function == "Martin and Gaddy":
        return martin_and_gaddy(chromosome.chromosome_value)

"""
