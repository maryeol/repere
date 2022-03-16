import matplotlib.pyplot as plt
import numpy as np

plt.ion() #turn on interactive mode
fig=plt.figure() #returns the Figure

i=1
x=list()
y=list()

while True:
    temp_y = i+30
    x.append(i)
    y.append(temp_y)
    plt.scatter(i, temp_y)  # to draw a scatter plot.
    i += 1
    plt.show()
    plt.pause(0.01)