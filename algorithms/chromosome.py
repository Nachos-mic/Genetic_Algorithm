import numpy as np
import random

class Chromosome:
    def __init__(self, number_of_bits, precision=0, random_init=True):
        self.number_of_bits = number_of_bits
        self.precision = precision
        self.chromosome_value = []
        if random_init:
            self.chromosome_value = np.random.randint(2, size=self.number_of_bits)

    def set_chromosome(self, chromosome_value):
        self.chromosome_value = chromosome_value

    def get_chromosome_len(self):
        return len(self.chromosome_value)

    def to_real_value(self, min_val, max_val):
        binary_str = ''.join(map(str, self.chromosome_value))
        integer_value = int(binary_str, 2)
        return min_val + (integer_value / (2 ** self.number_of_bits - 1)) * (max_val - min_val)

    def change_chromosome_bit(self, index):
        self.chromosome_value[index] = 1 - self.chromosome_value[index]