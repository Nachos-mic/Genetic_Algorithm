from algorithms.config import config
from algorithms.selection import best_selection, roulette_selection, tournament_selection
from algorithms.crossover import single_point_crossover, two_point_crossover, uniform_crossover
from algorithms.mutation import single_point_mutation, two_point_mutation, edge_mutation
from algorithms.inversion import inversion
from algorithms.fitness import evaluate_fitness
from algorithms.chromosome import Chromosome
from algorithms.individual import Individual
import random
import numpy as np
import time

def run_genetic_algorithm():

    population_size = config.population_size
    num_epochs = config.epochs
    crossover_rate = config.crossover_probability
    mutation_rate = config.mutation_probability
    inversion_rate = config.inversion_probability
    elitism_count = config.best_selection_amount
    selection_method = config.selection_method
    crossover_method = config.crossover_method
    num_variables = config.num_variables

    start_time = time.time()
    

    population = [Individual(num_variables=num_variables) for _ in range(population_size)]
    
    for ind in population:
        ind.evaluate()
    
    if config.optimization_type == "max":
        best_individual = max(population, key=lambda ind: ind.fitness)
        optimization_func = max
    else:
        best_individual = min(population, key=lambda ind: ind.fitness)
        optimization_func = min
    
    print(f"Epoka 0, najlepsze przystosowanie: {best_individual.fitness}")
    
    for generation in range(1, num_epochs + 1):

        if selection_method == "best":
            selected = best_selection(population, config.best_selection_amount)
        elif selection_method == "roulette":
            selected = roulette_selection(population, population_size)
        else:  
            selected = tournament_selection(population, tournament_size=config.tournament_size)
        

        if config.optimization_type == "max":
            elites = sorted(population, key=lambda ind: ind.fitness, reverse=True)[:elitism_count]
        else:
            elites = sorted(population, key=lambda ind: ind.fitness)[:elitism_count]
        

        new_population = []
        
        while len(new_population) < population_size - elitism_count:

            parent1 = random.choice(selected)
            parent2 = random.choice(selected)
            

            if random.random() < crossover_rate:
                for i in range(parent1.num_variables):
                    if crossover_method == "one_point":
                        child1_chrom, child2_chrom = single_point_crossover(
                            parent1.chromosomes[i].chromosome, 
                            parent2.chromosomes[i].chromosome
                        )
                    elif crossover_method == "two_point":
                        child1_chrom, child2_chrom = two_point_crossover(
                            parent1.chromosomes[i].chromosome, 
                            parent2.chromosomes[i].chromosome
                        )
                    else:  
                        child1_chrom, child2_chrom = uniform_crossover(
                            parent1.chromosomes[i].chromosome, 
                            parent2.chromosomes[i].chromosome
                        )
                    
                    if child1_chrom is not None and child2_chrom is not None:

                        if len(new_population) < population_size - elitism_count:
                            child1 = Individual(num_variables=num_variables, random_init=False)
                            for j in range(child1.num_variables):
                                if j == i:
                                    child1.chromosomes[j].set_chromosome(child1_chrom)
                                else:
                                    child1.chromosomes[j].set_chromosome(
                                        parent1.chromosomes[j].chromosome.copy()
                                    )
                            new_population.append(child1)
                        
                        if len(new_population) < population_size - elitism_count:
                            child2 = Individual(num_variables=num_variables, random_init=False)
                            for j in range(child2.num_variables):
                                if j == i:
                                    child2.chromosomes[j].set_chromosome(child2_chrom)
                                else:
                                    child2.chromosomes[j].set_chromosome(
                                        parent2.chromosomes[j].chromosome.copy()
                                    )
                            new_population.append(child2)
            else:

                if len(new_population) < population_size - elitism_count:
                    new_population.append(parent1)
                if len(new_population) < population_size - elitism_count:
                    new_population.append(parent2)
        

        for ind in new_population:
            if config.mutation_method == "one_point":
                ind.mutate(mutation_rate)
            elif config.mutation_method == "two_point":
                ind.mutate(mutation_rate, method="two_point")
            else: 
                ind.mutate(mutation_rate, method="edge")
        
        for ind in new_population:
            for i in range(ind.num_variables):
                ind.chromosomes[i].set_chromosome(
                    inversion(ind.chromosomes[i].chromosome, inversion_rate)
                )
        
        new_population.extend(elites)
        
        for ind in new_population:
            ind.evaluate()
        
        population = new_population

        current_best = optimization_func(population, key=lambda ind: ind.fitness)
        if (config.optimization_type == "max" and current_best.fitness > best_individual.fitness) or \
           (config.optimization_type == "min" and current_best.fitness < best_individual.fitness):
            best_individual = current_best
        
        if generation % 10 == 0:
            print(f"Epoka {generation}, najlepsze przystosowanie: {best_individual.fitness}")
    
    best_individual.evaluate() 


    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Czas wykonania algorytmu: {execution_time:.2f} sekund")

    return best_individual, execution_time



