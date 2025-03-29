import random
from algorithms.chromosome import Chromosome

def single_point_mutation(chromosome: Chromosome, probability: float = 1) -> None:
    if random.random() <= probability:
        mutation_point = random.randint(0, chromosome.get_chromosome_len() - 1)
        chromosome.change_chromosome_bit(mutation_point)