import random
from matplotlib import pyplot as plt
from OneMax import create_individual, crossover, mutate, geneticAlgo

generations = 30


def evaluate(input_string):
    num_ones = sum(int(bit) for bit in input_string)

    if num_ones > 0:
        return num_ones
    else:
        return 2 * len(input_string)


avg_fitness_values = geneticAlgo(30, 50, generations, 0.05)

# Plot the average fitness over generations
plt.plot(range(1, generations + 1), avg_fitness_values, marker='o')
plt.xlabel('Generation')
plt.ylabel('Average Fitness')
plt.title('1.3 Average Fitness Over Generations')
plt.show()
