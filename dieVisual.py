from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# Creating a D6 dice.
die = Die()

# Making some results of six-sided dice rolls, and storing the results in a list.
results = []
for roll_num in range(2000):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
# print(results)  # With this we can the result of any roll.
# print(frequencies)  # With this we can see how many times each number was the result.
# With the list of frequencies, we can make a Histogram of the results.

# Visualize the results.
x_values = list(range(1, die.num_sides + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 2000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
