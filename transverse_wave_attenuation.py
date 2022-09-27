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
symbol = 0.5
def animate_points_attenuation(i):
    ax.clear()
    # Get the point from the points list at index i
    # Plot that point using the x and y coordinates
    # Set the x and y axis to display a fixed range
    for x,y in data:
        finalY = (math.e ** (-symbol * i) * math.cos(math.sqrt(1 -symbol**2) * x * i)) + y
        ax.plot(x, finalY, color='green', marker='o')
    
    ax.set_xlim([0, 5])
    ax.set_ylim([-1, 2])

anim = FuncAnimation(fig, animate_points_attenuation, frames = 30, interval=500, repeat=False)
plt.close()
anim.save("transverse_wave_attenuation.gif", dpi=300, writer=PillowWriter(fps=5))
print("done")