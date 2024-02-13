from plotly.graph_objs import Bar, Layout
from plotly import offline
from dice import Die

"""2. Three Dice"""
dice1 = Die()
dice2 = Die()
dice3 = Die()

results = []
# for roll_num in range(1000):
for roll_num in range(1000):
    result = dice1.roll() + dice2.roll() + dice3.num_sides
    results.append(result)

frequencies = []
maxRe = dice1.num_sides + dice2.num_sides + dice3.num_sides
for value in range(1, maxRe + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(1, maxRe + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling three D6 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6_d6.html')
"""I can see that there is 3 results, that we most likely get when rolling
   three of D6, 1000 times, there are six ways to roll a 12,13,14,
   Therefore, these are the most common results, and you’re equally likely to roll any one of
   these numbers, with the loop down you can check/see the sum of all the ways to make those results."""
# results_count = 0
# for dice1 in range(1, 7):
#     for dice2 in range(1, 7):
#         for dice3 in range(1, 7):
#             total = dice1 + dice2 + dice3
#             # If the total is one of the desired results, increment its count
#             if total in results_count:
#                 results_count[total] += 1
# print(results_count)
# """{12: 25, 13: 21, 14: 15}"""
