# Analysis-on-rolling-a-dice

This project simulates rolling a six-sided die (D6) or more/less (D4, D8..) and visualizes the outcomes using Plotly. 
The simulation a chosen rolls die 2000 times (or more), calculates the frequency of each result, and then plots these frequencies in a histogram.

<img width="600" alt="htmlPic_Histogram_Of_2RollDice" src="https://github.com/Masanbat12/Analysis-on-rolling-a-dice/assets/93978448/00f92248-605e-4afd-b704-462aada9a869">


## Project Structure:
The project consists of two main files, and any other file check other tasks, like what i got if i change the  dice from D6 to D4 or D8,
so that there will be more understandig of the data i getting from the histogram.
Some of the information I can extract from the data shown in the histogram,
Which result i most likely will get from rolling two dice.
You can see how the calculation is done in [diceVisual.py📂](https://github.com/Masanbat12/Analysis-on-rolling-a-dice/blob/main/dieVisual.py).

## Two main class that the project was base on:
##### dice.py
This file defines a Die class used to simulate a die with a customizable number of sides,
defaulting to a six-sided die. The roll method returns a random value between 1 and the number of sides on the die.

##### diceVisual.py
This class performs the die-rolling simulation, calculates the frequency of each outcome,
and generates a histogram using Plotly to visualize these frequencies.

### Requirements:
To run this project, you will need Python3 and the following packages:
##### plotly: Used for creating the histogram visualization.
pip install plotly
##### matplotlib: Used for creating static, interactive, and animated visualizations in Python.
pip install matplotlib


### Installation:
Ensure you have Python 3 installed on your system.

# Usage:
To run the die-rolling and the other file's of simulation and to generate the visualization
"file_name".py

You all can see the results of me run the programs in the: [Pics of results 📂](https://github.com/Masanbat12/Analysis-on-rolling-a-dice/tree/main/Pics%20of%20results)
[html's files as results 📂](https://github.com/Masanbat12/Analysis-on-rolling-a-dice/tree/main/html's%20files%20as%20results)



