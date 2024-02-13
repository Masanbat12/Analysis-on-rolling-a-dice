from plotly.graph_objs import Bar, Layout
from plotly import offline
from dice import Dice

"""3. Multiplication:"""
# Creating 2 dice of D6 and D8 dice.
dice1 = Dice(4)
dice2 = Dice(4)

# Making some results of rolling six-sided dice, and storing the results in a list.
results = []
for roll_num in range(1000):
    result = dice1.roll() * dice2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
maxRe = dice1.num_sides * dice2.num_sides
for value in range(1, maxRe + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(1, maxRe + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Multiplication_Result'}
y_axis_config = {'title': 'Frequency of Multiplication_Result'}
# my_layout = Layout(title='Results of rolling two D8 1000 times',
my_layout = Layout(title='Multiplication_Results of rolling two D4 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d4_d4.html')

