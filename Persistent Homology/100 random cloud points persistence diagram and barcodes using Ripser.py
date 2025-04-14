# -*- coding: utf-8 -*-

# Based on the method used in ripser.py by Ulrich Bauer

# "pip install ripser" in terminal to install risper
import ripser
import numpy as np
import matplotlib.pyplot as plt

# Generate a random point cloud
# We first randomly generate 100 points in 2D space
points =  np.random.rand(100,2)

# Because it is randomly generated, each time it will give us different point, to make sure they give us the same points each tme we ran the code, we would randomly set seed as 30
np.random.seed(30) 

# [:,0] means taking all x values
# [:,0] means taking all y values
# We are setting the colour of our points as black then we plot the scatter diagram showing our points
plt.scatter(points[:, 0], points[:, 1], c='black')  
plt.title('100 Random Cloud Points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()

# Compute persistent homology
results = ripser.ripser(points, maxdim=1)  # Compute H0 and H1, by setting maxdim to 1 we would only be computing persistence diagram up to dimension 1
diagrams = results['dgms']  # Extract persistence diagrams

# Since dgms contains results for different dimensions, we have seperated them as H0 and H1 
H0 = results['dgms'][0] 
H1 = results['dgms'][1] 

# Now we plot the perssitence diagram
def plot_diagram(diagram, label, color):
    plt.scatter(diagram[:, 0], diagram[:, 1], label=label, color=color)
    plt.plot([0, 1], [0, 1], linestyle= '--')  # Plot a dashed diagonal line

# plotting persistence diagram
plt.figure(figsize=(8, 6))
plot_diagram(H0, "H0", "blue")
plot_diagram(H1, "H1", "red")
plt.title("Persistence Diagram")
plt.xlabel("Birth")
plt.ylabel("Death")
plt.legend()
plt.show()

#Plot barcodes
def plot_barcode(diagram, title, y_label, color):
    plt.figure(figsize=(8, 4))
    for i in range(len(diagram)):
        birth = diagram[i][0] # we are defining birth of i to be the column 0 of diagram
        death = diagram[i][1] # we are defining death of i to be the column 1 of diagram
        plt.plot([birth, death], [i, i], color=color)  # Plot horizontal lines
    plt.title(title) #Title added later, different for two barcodes
    plt.xlabel("Filtration Value") # Label x axis
    plt.yticks([])  # Hide y-axis values
    plt.ylabel(y_label)  # Add custom y-axis label
    plt.grid(True, axis='x')  # Only add value on the x-axis
    plt.show()


# Plot H0 barcode
plot_barcode(H0, "Barcode Plot for H0", "H0", "blue")

# Plot H1 barcode
plot_barcode(H1, "Barcode Plot for H1", "H1", "red")
