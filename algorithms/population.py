import random
import numpy as np
from algorithms.individual import Individual


class Population:
    def __init__(self, size, num_variables, bits_per_variable, precision=0):

        self.individuals = []
        self.size = size
        self.generation = 0
        self.num_variables = num_variables
        self.bits_per_variable = bits_per_variable
        self.precision = precision

        for _ in range(size):
            self.individuals.append(Individual(num_variables, bits_per_variable, precision))
    
    def evaluate_all(self, fitness_func, bounds):
        for individual in self.individuals:
            individual.evaluate(fitness_func, bounds)
    
    def select_tournament(self, tournament_size=3):
        tournament = random.sample(self.individuals, tournament_size)
        return max(tournament, key=lambda ind: ind.fitness)
    
    def single_point_crossover(self, parent1, parent2):
        offspring1 = Individual(self.num_variables, self.bits_per_variable, self.precision, False)
        offspring2 = Individual(self.num_variables, self.bits_per_variable, self.precision, False)
        
        for i in range(self.num_variables):
            chrom_len = parent1.chromosomes[i].get_chromosome_len()
            
            crossover_point = random.randint(1, chrom_len - 1)
            
            child1_value = np.concatenate((parent1.chromosomes[i].chromosome_value[:crossover_point], 
                                         parent2.chromosomes[i].chromosome_value[crossover_point:]))
            child2_value = np.concatenate((parent2.chromosomes[i].chromosome_value[:crossover_point], 
                                         parent1.chromosomes[i].chromosome_value[crossover_point:]))
            
            offspring1.chromosomes[i].set_chromosome(child1_value)
            offspring2.chromosomes[i].set_chromosome(child2_value)
        
        return offspring1, offspring2
    
    def evolve(self, fitness_func, bounds, crossover_rate=0.8, mutation_rate=0.01, tournament_size=3, elitism=True):
        self.evaluate_all(fitness_func, bounds)
        
        self.individuals.sort(key=lambda ind: ind.fitness, reverse=True)
        
        new_population = []
        
        if elitism:
            new_population.append(self.individuals[0])
        
        while len(new_population) < self.size:
            parent1 = self.select_tournament(tournament_size)
            parent2 = self.select_tournament(tournament_size)
            
            if random.random() < crossover_rate:
                offspring1, offspring2 = self.single_point_crossover(parent1, parent2)
            else:
                offspring1, offspring2 = parent1, parent2
            
            offspring1.mutate(mutation_rate)
            offspring2.mutate(mutation_rate)
            
            new_population.append(offspring1)
            if len(new_population) < self.size:
                new_population.append(offspring2)
        
        self.individuals = new_population[:self.size]
        self.generation += 1
    
    def run(self, fitness_func, bounds, max_generations=100, crossover_rate=0.8, 
            mutation_rate=0.01, tournament_size=3, elitism=True):
        best_fitness_history = []
        avg_fitness_history = []
        
        for gen in range(max_generations):
            self.evolve(fitness_func, bounds, crossover_rate, mutation_rate, tournament_size, elitism)
            
            best_fitness = max(ind.fitness for ind in self.individuals)
            avg_fitness = sum(ind.fitness for ind in self.individuals) / self.size
            
            best_fitness_history.append(best_fitness)
            avg_fitness_history.append(avg_fitness)
            
            print(f"Pokolenie {gen+1}/{max_generations}: Najlepsze przystosowanie = {best_fitness:.6f}, Średnie przystosowanie = {avg_fitness:.6f}")
        
        best_individual = max(self.individuals, key=lambda ind: ind.fitness)
        return best_individual, best_fitness_history, avg_fitness_history
