import random
from matplotlib import pyplot as plt
from main import create_individual, crossover, mutate, geneticAlgo

# Set a seed for reproducibility
random.seed(42)

length = 30
generations = 100
target_string = ''.join(random.choice(['0', '1']) for _ in range(length))
print(target_string)


def evaluate(input_string):
    output = sum(bit == target_bit for bit, target_bit in zip(input_string, target_string))
    return output


avg_fitness_values = geneticAlgo(length, 50, generations, 0.05)

# Plot the average fitness over generations
plt.plot(range(1, generations + 1), avg_fitness_values, marker='o')
plt.xlabel('Generation')
plt.ylabel('Average Fitness')
plt.title('1.2 Average Fitness Over Generations')
plt.show()