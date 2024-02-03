import random
from main import crossover

generations = 1

with open('BPP1.txt', 'r') as file:
    lines = file.readlines()

m = int(lines[0].strip())  # Number m of different item weights
C = int(lines[1].strip())  # Capacity C of the bins

item_weights = []
item_counts = []

for line in lines[2:]:
    weight, count = map(int, line.strip().split())
    item_weights.append(weight)
    item_counts.append(count)


def initialize_population():

    population = []
    for weight, count in zip(item_weights, item_counts):
        items = [weight] * count
        population.extend(items)

    # Randomly shuffle the items in the solution
    random.shuffle(population)

    return population


def evaluate(bins):
    return(len(bins))


def binning(population):
    solution = []
    bin_item = []
    remaining_capacity = C

    for item in population:
        if remaining_capacity - item >= 0:
            bin_item.append(item)
            remaining_capacity -= item
        else:
            solution.append(bin_item)
            bin_item = []
            remaining_capacity = C

    # Add the last bin if it's not empty
    if bin_item:
        solution.append(bin_item)

    return solution


#def crossover(parent1, parent2):


population = initialize_population()
bins = binning(population)

fitness_values = []

for generation in range(generations):
    # Get fitness for the generation
    fitness = evaluate(bins)
    fitness_values.append(fitness)

    print(f"Generation {generation + 1}: Fitness = {fitness}")

    print(bins)
    # Select parents
    parent1 = random.randint(1, fitness)
    parent2 = random.randint(1, fitness)
    print(parent1)
    print(parent2)

    # Create offspring
    child1, child2 = crossover(bins[parent1-1], bins[parent2-1])
    print(child1)
    print(child2)
    bins[parent1-1] = child1
    bins[parent2-1] = child2

    print(bins)