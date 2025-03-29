def inversion(chromosome, probability=0.1):
    if random.random() <= probability:
        start, end = sorted(random.sample(range(chromosome.get_chromosome_len()), 2))
        chromosome.chromosome_value[start:end + 1] = reversed(chromosome.chromosome_value[start:end + 1])
