import random

def best_selection(population, num_selected):
    sorted_population = sorted(population, key=lambda ind: ind.fitness)
    return sorted_population[:num_selected]

def roulette_selection(population, num_selected):
    total_fitness = sum(1/ind.fitness for ind in population)
    selection_probs = [(1/ind.fitness)/total_fitness for ind in population]
    
    selected = []
    for _ in range(num_selected):
        r = random.random()
        cumulative_prob = 0
        for i, ind in enumerate(population):
            cumulative_prob += selection_probs[i]
            if r <= cumulative_prob:
                selected.append(ind)
                break
    return selected

def tournament_selection(population, tournament_size=3):
    selected = []
    for _ in range(len(population)):
        tournament = random.sample(population, tournament_size)
        winner = min(tournament, key=lambda ind: ind.fitness)
        selected.append(winner)
    return selected
