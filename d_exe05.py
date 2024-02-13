import matplotlib.pyplot as plt
from random import randint

"""5. Practicing with Both Libraries:"""


def roll_die(num_rolls):
    results = [randint(1, 6) for _ in range(num_rolls)]
    return results


# Simulate rolling a D6 dice 100 times
rolls = 100
results = roll_die(rolls)

# Calculate frequencies
frequencies = [results.count(value) for value in range(1, 7)]

# Visualize the results
plt.figure(figsize=(10, 6))
plt.bar(range(1, 7), frequencies, color='blue', edgecolor='black')

plt.title('Die Rolling Frequencies')
plt.xlabel('Die Value')
plt.ylabel('Frequency')
plt.xticks(range(1, 7))  # Set x-ticks to match die values
plt.show()
