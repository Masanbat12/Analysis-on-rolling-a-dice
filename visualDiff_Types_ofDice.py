from plotly.graph_objs import Bar, Layout
from plotly import offline
from dice import Dice

# Creating 2 dice of D6 and D8 dice.
dice1 = Dice()
dice2 = Dice(8)

# Making some results of rolling six-sided dice, and storing the results in a list.
results = []
for roll_num in range(40_000):
    result = dice1.roll() + dice2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
maxR = dice1.num_sides + dice2.num_sides
for value in range(1, maxR + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(1, maxR + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling a D6 and D8 40000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d8.html')
