# Dampened/Undampened System plot
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math 
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter

fig, ax = plt.subplots(1, 1)
fig.set_size_inches(5,5)

# generate random points on interval
xData = np.random.uniform(0, 5, 100)
yData = np.random.uniform(0, 1, 100)
data = np.stack((xData,yData), axis = -1)

def animate_points(i):
    ax.clear()
    # Get the point from the points list at index i
    # Plot that point using the x and y coordinates
    # Set the x and y axis to display a fixed range
    for x,y in data:
        finalX = math.cos(x + i) + x
        ax.plot(finalX, y, color='green', marker='o')
    
    ax.set_xlim([-1, 6])
    ax.set_ylim([-1, 2])
        


ani = FuncAnimation(fig, animate_points, frames= 100, interval=500, repeat=True)
plt.close()
ani.save("longitudinal_wave.gif", dpi=300, writer=PillowWriter(fps=5))
print("done")