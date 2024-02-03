from matplotlib import pyplot as plt
from main import geneticAlgo

generations = 30

avg_fitness_values = geneticAlgo(30, 50, generations, 0.05)

# Plot the average fitness over generations
plt.plot(range(1, generations + 1), avg_fitness_values, marker='o')
plt.xlabel('Generation')
plt.ylabel('Average Fitness')
plt.title('1.1 Average Fitness Over Generations')
plt.show()