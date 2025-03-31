import random
import numpy as np

class Chromosome:
    def __init__(self, num_bits=25, random_init=True):
        self.num_bits = num_bits
        self.chromosome_value = None
        
        if random_init:
            self.chromosome = [random.randint(0, 1) for _ in range(self.num_bits)]
        else:
            self.chromosome = [0] * self.num_bits
            
    def set_chromosome(self, chromosome):
        self.chromosome = chromosome
        
    def decode(self, a=-10, b=10):
        decimal_value = 0
        for i in range(self.num_bits):
            decimal_value += self.chromosome[i] * (2 ** (self.num_bits - 1 - i))
        
        x = a + decimal_value * (b - a) / (2**self.num_bits - 1)
        self.chromosome_value = x
        return x
        
    def mutate(self, position):
        if 0 <= position < self.num_bits:
            self.chromosome[position] = 1 - self.chromosome[position]
