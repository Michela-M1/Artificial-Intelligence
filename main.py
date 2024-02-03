import random


def create_individual(length):
    # Generate a random string of 30 characters with 1s and 0s
    return ''.join(random.choice(['0', '1']) for _ in range(length))


def evaluate(input_string):
    return input_string.count('1')


def crossover(parent1, parent2):
    x = random.randint(1, len(parent1) - 1)
    child1 = parent1[:x] + parent2[x:]
    child2 = parent2[:x] + parent1[x:]
    return child1, child2


def mutate(individual, mutation_rate):
    mutated_individual = ""
    for bit in individual:
        if random.random() < mutation_rate:
            # Flip the bit
            mutated_individual += "0" if bit == "1" else "1"
        else:
            mutated_individual += bit
    return mutated_individual


def geneticAlgo(length, pop_size, generations, mutation_rate):
    # Create the population
    population = [create_individual(length) for _ in range(pop_size)]
    avg_fitness_values = []

    for generation in range(generations):
        # Evaluate fitness
        fitness_values = [evaluate(individual) for individual in population]

        # Get average fitness for the generation
        avg_fitness = sum(fitness for fitness in fitness_values) / pop_size
        avg_fitness_values.append(avg_fitness)
        print(f"Generation {generation + 1}: Average Fitness = {avg_fitness}")

        # Select parents
        selected_parents = random.choices(population, weights=fitness_values, k=pop_size)

        # Create offspring
        offspring = []
        for i in range(0, pop_size, 2):
            parent1, parent2 = selected_parents[i], selected_parents[i+1]
            child1, child2 = crossover(parent1, parent2)
            offspring.extend(mutate(child, mutation_rate) for child in (child1, child2))

        # Replace old population with new one
        population = [child for child in offspring]

    return avg_fitness_values