import random
from main import crossover

# Set a seed for reproducibility
random.seed(42)

generations = 50
pop_size = 30
mutation_rate = 0.1

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
    bins_used = 0
    current_bin_capacity = C

    for item_weight in individual:
        if item_weight <= current_bin_capacity:
            current_bin_capacity -= item_weight
        else:
            bins_used += 1
            current_bin_capacity = C - item_weight

    if current_bin_capacity < C:
        bins_used += 1
    return bins_used


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

population = initialize_population(pop_size, item_weights, item_counts)
avg_fitness_values = []
lowest_fitness = 100
best_individual = None

for generation in range(generations):
    # Evaluate fitness
    fitness_values = []
    for individual in population:
        fitness = evaluate(individual)
        fitness_values.append(fitness)

        if (fitness < lowest_fitness):
            lowest_fitness = fitness
            best_individual = individual
            print("Fitness:", lowest_fitness, "Best individual:", best_individual)
    #fitness_values = [evaluate(individual) for individual in population]

    # Get average fitness for the generation
    avg_fitness = sum(fitness for fitness in fitness_values) / pop_size
    avg_fitness_values.append(avg_fitness)
    print(f"Generation {generation + 1}: Average Fitness = {avg_fitness}")

    # Select parents
    selected_parents = []
    for i, fitness in enumerate(fitness_values):
        # Only select parents for crossover if their fitness is above the average
        if fitness >= avg_fitness:
            selected_parents.append(population.pop(i))
            fitness_values.pop(i)
    # If the selected population is odd, randomly remove one
    if len(selected_parents) % 2 != 0:
        random_index = random.randint(0, len(selected_parents) - 1)
        population.append(selected_parents.pop(random_index))

    # Create offspring
    offspring = []
    for i in range(0, len(selected_parents), 2):
        parent1 = selected_parents[i]
        parent2 = selected_parents[i + 1]
        child1, child2 = crossover(parent1, parent2)
        offspring.extend(mutation(child) for child in (child1, child2))

    # Combine offspring with the rest of the population
    new_population = population + offspring

    # Update population with offspring
    population = new_population

print("Lowest fitness:", lowest_fitness, "Best individual:", best_individual)