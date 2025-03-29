from configuration import config
from selection_methods import best_selection, roulette_selection, tournament_selection
from cross_methods import single_point_crossover, two_point_crossover
from mutation import single_point_mutation, two_point_mutation, edge_mutation
from inversion import inversion
from fitness_functions import evaluate_fitness

def run_genetic_algorithm():
    population = [Chromosome(config.num_variables) for _ in range(config.population_size)]

    for epoch in range(config.epochs):
        fitness_values = [evaluate_fitness(ind) for ind in population]

        if config.selection_method == "best":
            selected_population = best_selection(population, fitness_values, config.best_selection_amount)
        elif config.selection_method == "roulette":
            selected_population = roulette_selection(population, fitness_values)
        elif config.selection_method == "tournament":
            selected_population = tournament_selection(population, fitness_values, config.tournament_size)

        new_population = []
        for i in range(0, len(selected_population), 2):
            if random.random() <= config.crossover_probability:
                if config.crossover_method == "one_point":
                    child1, child2 = single_point_crossover(selected_population[i], selected_population[i+1])
                elif config.crossover_method == "two_point":
                    child1, child2 = two_point_crossover(selected_population[i], selected_population[i+1])
                new_population.extend([Chromosome(config.num_variables, False) for _ in (child1, child2)])
            else:
                new_population.extend([selected_population[i], selected_population[i+1]])

        for individual in new_population:
            if random.random() <= config.mutation_probability:
                if config.mutation_method == "one_point":
                    single_point_mutation(individual)
                elif config.mutation_method == "two_point":
                    two_point_mutation(individual)
                elif config.mutation_method == "edge":
                    edge_mutation(individual)

            inversion(individual, config.inversion_probability)

        population = new_population

    return min(population, key=evaluate_fitness)  # Minimalizacja
