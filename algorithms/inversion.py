import random

def inversion(chromosome, inversion_rate=0.3):
    if random.random() < inversion_rate:
        length = len(chromosome)
        point1 = random.randint(0, length - 2)
        point2 = random.randint(point1 + 1, length - 1)
        
        segment = chromosome[point1:point2 + 1]
        segment.reverse()
        
        new_chromosome = chromosome[:point1] + segment + chromosome[point2 + 1:]
        
        return new_chromosome
    return chromosome
