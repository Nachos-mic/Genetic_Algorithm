def genetic_algorithm(config, minimize=True):
    population = initialize_population(config.population_size)
    best_solution = None
    for _ in range(config.num_epochs):
        population = evaluate_fitness(population, minimize)
        new_population = []
        if config.elitism:
            best_solution = min(population, key=lambda x: x.fitness) if minimize else max(population, key=lambda x: x.fitness)
            new_population.append(best_solution)
        while len(new_population) < config.population_size:
            parent1, parent2 = select_parents(population)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])
        population = new_population[:config.population_size]