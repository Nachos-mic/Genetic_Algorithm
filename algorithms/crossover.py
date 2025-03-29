import numpy as np
import random

def single_point_crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
    child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
    return child1, child2


def two_point_crossover(self, parent1, parent2):
    points = sorted(random.sample(range(1, self.num_variables), 2))
    p1, p2 = points
    child1 = np.concatenate((parent1[:p1], parent2[p1:p2], parent1[p2:]))
    child2 = np.concatenate((parent2[:p1], parent1[p1:p2], parent2[p2:]))
    return child1, child2


def uniform_crossover(self, parent1, parent2):
    mask = np.random.rand(self.num_variables) < 0.5
    child1 = np.where(mask, parent1, parent2)
    child2 = np.where(mask, parent2, parent1)
    return child1, child2


def granular_crossover(self, parent1, parent2):
    alpha = np.random.rand(self.num_variables)
    child1 = alpha * parent1 + (1 - alpha) * parent2
    child2 = (1 - alpha) * parent1 + alpha * parent2
    return child1, child2
