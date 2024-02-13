import plotly.graph_objs as go
import plotly.offline as pyo
from random import choice


# Function to generate a random walk
def random_walk(steps):
    # Start with (0, 0)
    x, y = [0], [0]

    for _ in range(steps):
        x_direction = choice([1, -1])
        x_distance = choice([0, 1, 2, 3, 4])
        x_step = x_direction * x_distance

        y_direction = choice([1, -1])
        y_distance = choice([0, 1, 2, 3, 4])
        y_step = y_direction * y_distance

        next_x = x[-1] + x_step
        next_y = y[-1] + y_step

        x.append(next_x)
        y.append(next_y)

    return x, y


# Generate a random walk
steps = 500
x, y = random_walk(steps)

# Create a scatter plot for the random walk
trace = go.Scatter(x=x, y=y, mode='markers+lines', name='Random Walk')
data = [trace]

# Define layout
layout = go.Layout(title='Random Walk', xaxis={'title': 'Step'}, yaxis={'title': 'Distance'})

# Plot the random walk
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='random_walk.html')
