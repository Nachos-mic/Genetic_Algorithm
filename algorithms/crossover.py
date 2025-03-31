import random

def single_point_crossover(parent1, parent2):
    if parent1 is None or parent2 is None:
        print("Ostrzeżenie: Jeden z rodziców jest None")
        return None, None
        
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def two_point_crossover(parent1, parent2):
    if parent1 is None or parent2 is None:
        print("Ostrzeżenie: Jeden z rodziców jest None")
        return None, None
        
    length = len(parent1)
    point1 = random.randint(1, length - 2)
    point2 = random.randint(point1 + 1, length - 1)
    
    child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]
    return child1, child2

def uniform_crossover(parent1, parent2):
    if parent1 is None or parent2 is None:
        print("Ostrzeżenie: Jeden z rodziców jest None")
        return None, None
        
    child1 = []
    child2 = []
    for i in range(len(parent1)):
        if random.random() < 0.5:
            child1.append(parent1[i])
            child2.append(parent2[i])
        else:
            child1.append(parent2[i])
            child2.append(parent1[i])
    return child1, child2
