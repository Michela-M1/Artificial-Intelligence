import random

# Set a seed for reproducibility
random.seed(42)

length = 30


def create_individual():
    # Generate a random string of 30 characters with 1s and 0s
    return ''.join(random.choice(['0', '1']) for _ in range(length))


def evaluate(input_string):
    return input_string.count('1')


def crossover(parent1, parent2):
    # Choose a random crossover point
    x = random.randint(0, len(parent1) - 1)     # if x is 0 or 29, then there is no crossover...

    # Perform one-point crossover
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
