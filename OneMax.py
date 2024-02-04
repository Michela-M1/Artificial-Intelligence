import random
from matplotlib import pyplot as plt
from main import create_individual, evaluate, crossover, mutate

# Set a seed for reproducibility
random.seed(42)

pop_size = 100
generations = 30
mutation_rate = 0.05


# Create the population
population = [create_individual() for _ in range(pop_size)]
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
    for i in range(0, len(selected_parents), 2):
        parent1, parent2 = selected_parents[i], selected_parents[i + 1]
        child1, child2 = crossover(parent1, parent2)
        offspring.extend(mutate(child, mutation_rate) for child in (child1, child2))

    # Update population with offspring
    population = offspring
    print(f"pop: {population}")

# Plot the average fitness over generations
plt.plot(range(1, generations + 1), avg_fitness_values, marker='o')
plt.xlabel('Generation')
plt.ylabel('Average Fitness')
plt.title('1.1 Average Fitness Over Generations')
plt.show()