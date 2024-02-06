import random
# Set a seed for reproducibility
random.seed(42)

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Extract data from lines
    m = int(lines[0])   # Number m of different item weights
    C = int(lines[1])   # Capacity C of the bins

    item_weights = []
    item_counts = []
    for line in lines[2:]:
        weight, count = map(int, line.strip().split())
        item_weights.append(weight)
        item_counts.append(count)

    return m, C, item_weights, item_counts


def initialize_population(population_size, item_weights, item_counts):
    population = []
    for _ in range(population_size):
        # Generate a random solution based on item weights and counts
        solution = []
        for weight, count in zip(item_weights, item_counts):
            items = [weight] * count
            solution.extend(items)
        random.shuffle(solution)
        population.append(solution)
    return population


def evaluate(individual):
    total_weight = 0
    bins_used = 0
    current_bin_capacity = C

    for item_weight in individual:
        if item_weight <= current_bin_capacity:
            current_bin_capacity -= item_weight
        else:
            bins_used += 1
            current_bin_capacity = C - item_weight

    # Consider the last bin if not completely filled
    if current_bin_capacity < C:
        bins_used += 1

    return bins_used


def parents_selection(population, fitness_values, average_fitness):
    selected_parents_for_crossover = []

    for i, fitness in enumerate(fitness_values):
        # Only select parents for crossover if their fitness is below the average
        if fitness > average_fitness:
            selected_parents_for_crossover.append(population.pop(i))
            fitness_values.pop(i)

    # If the selected population is odd, randomly select one additional parent
    if len(selected_parents_for_crossover) % 2 != 0:
        random_index = random.randint(0, len(selected_parents_for_crossover) - 1)
        population.append(selected_parents_for_crossover.pop(random_index))

    # Perform crossover on selected parents
    offspring = []
    for i in range(0, len(selected_parents_for_crossover), 2):
        parent1 = selected_parents_for_crossover[i]
        parent2 = selected_parents_for_crossover[i + 1]
        child1, child2 = crossover_function(parent1, parent2)
        offspring.extend(mutation(child) for child in (child1, child2))

    # Combine offspring with the rest of the population
    new_population = population + offspring

    return new_population


def crossover_function(parent1, parent2):
    # Choose a random crossover point
    crossover_point = random.randint(1, min(len(parent1), len(parent2)) - 1)

    # Perform one-point crossover
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]

    return child1, child2


def mutation(bins):

    mutated_bins = bins.copy()
    for i in range(len(mutated_bins)):
        if random.random() < mutation_rate:
            new_position = random.randint(0, len(mutated_bins) - 1)
            mutated_bins[i] = bins[new_position]
            mutated_bins[i] = bins[i]

    return mutated_bins


file_path = 'BPP1.txt'
m, C, item_weights, item_counts = read_data_from_file(file_path)

generations = 100
pop_size = 20
mutation_rate = 0.1
population = initialize_population(pop_size, item_weights, item_counts)
avg_fitness_values = []

for generation in range(generations):
    # Evaluate fitness
    fitness_values = [evaluate(individual) for individual in population]

    # Get average fitness for the generation
    avg_fitness = sum(fitness for fitness in fitness_values) / pop_size
    avg_fitness_values.append(avg_fitness)
    print(f"Generation {generation + 1}: Average Fitness = {avg_fitness}")

    # Do crossover AND MUTATION
    population = parents_selection(population, fitness_values, avg_fitness)

