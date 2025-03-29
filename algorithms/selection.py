def tournament_selection(population, k=3):
    selected = random.sample(population, k)
    return max(selected, key=lambda chromo: chromo.fitness)

"""
def best_selection(population, fitness_values, num_selected):
    sorted_indices = np.argsort(fitness_values)  # Sortowanie wg fitness
    return [population[i] for i in sorted_indices[:num_selected]]

def roulette_selection(population, fitness_values):
    total_fitness = sum(fitness_values)
    selection_probs = [f / total_fitness for f in fitness_values]
    return random.choices(population, weights=selection_probs, k=len(population))

def tournament_selection(population, fitness_values, tournament_size):
    selected = []
    for _ in range(len(population)):
        tournament = random.sample(list(zip(population, fitness_values)), tournament_size)
        winner = min(tournament, key=lambda x: x[1])[0]  # Minimalizacja
        selected.append(winner)
    return selected


"""