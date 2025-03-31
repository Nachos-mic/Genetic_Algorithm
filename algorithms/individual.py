from algorithms.chromosome import Chromosome
from algorithms.config import config
import random

class Individual:
    def __init__(self, num_variables=2, random_init=True):
        self.num_variables = num_variables
        self.chromosomes = [Chromosome(num_bits=config.precision, random_init=random_init) for _ in range(num_variables)]
        self.fitness = float('inf')
        self.chromosome_value = []  
        
    def evaluate(self):
        self.chromosome_value = []  
        for chromosome in self.chromosomes:
            value = chromosome.decode(a=config.range_start, b=config.range_end)
            self.chromosome_value.append(value)
        
        if len(self.chromosome_value) >= 2:
            x1, x2 = self.chromosome_value[:2]
            self.fitness = (x1 - x2)**2 + ((x1 + x2 - 10)/3)**2
        else:
            self.fitness = float('inf') 
        
        return self.fitness

    def mutate(self, mutation_rate=0.3, method="one_point"):
        """Mutacja wszystkich chromosomów"""
        for chromosome in self.chromosomes:
            if random.random() < mutation_rate:
                position = random.randint(0, chromosome.num_bits - 1)
                if method == "one_point":
                    chromosome.mutate(position)
                elif method == "two_point":
                    position2 = random.randint(0, chromosome.num_bits - 1)
                    chromosome.mutate(position)
                    chromosome.mutate(position2)
                elif method == "edge":
                    chromosome.mutate(0) 
                    chromosome.mutate(chromosome.num_bits - 1) 
