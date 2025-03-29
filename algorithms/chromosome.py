import numpy as np
import random

class Chromosome:
    def __init__(self, number_of_bits, random_init=True):
        self.number_of_bits = number_of_bits
        self.chromosome_value = []
        if random_init:
            self.chromosome_value = np.random.randint(2, size=self.number_of_bits)

    def set_chromosome(self, chromosome_value):
        self.chromosome_value = chromosome_value

    def get_chromosome_len(self):
        return len(self.chromosome_value)

    def change_chromosome_bit(self, index):
        self.chromosome_value[index] = 1 - self.chromosome_value[index]