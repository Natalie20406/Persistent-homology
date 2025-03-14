#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 12:44:28 2025

@author: natalie
"""

# "pip install ripser" in terminal to install risper
import ripser
import numpy as np
import matplotlib.pyplot as plt

# Generate a random point cloud
# Setting a seed to ensure it generates the same random numbers each time
np.random.seed(30) 
# Generate 100 points in 2D
points = np.random.rand(100, 2)

plt.scatter(points[:, 0], points[:, 1], c='blue')  
plt.title('Random Cloud Points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()

# Compute persistent homology
results = ripser.ripser(points, maxdim=1)  # Compute H0 and H1
diagrams = results['dgms']  # Extract persistence diagrams

h0_diagram = results['dgms'][0]  # H0 diagram (connected components)
h1_diagram = results['dgms'][1]  # H1 diagram (loops)

def plot_diagram(diagram, label, color):
    plt.scatter(diagram[:, 0], diagram[:, 1], label=label, color=color)
    plt.plot([0, 1], [0, 1], 'k--')  # Diagonal

plt.figure(figsize=(8, 6))
plot_diagram(h0_diagram, "H0", "blue")
plot_diagram(h1_diagram, "H1", "red")
plt.title("Persistence Diagram")
plt.xlabel("Birth")
plt.ylabel("Death")
plt.legend()
plt.show()

# Compute barcodes
# Function to plot barcodes
def plot_barcode(diagram, title, y_label, color):
    plt.figure(figsize=(8, 4))
    for i, (birth, death) in enumerate(diagram):
        plt.plot([birth, death], [i, i], color=color, linewidth=2)  # Plot horizontal lines at unique y-positions
    plt.title(title)
    plt.xlabel("Filtration Value")
    plt.yticks([])  # Hide y-axis values
    plt.ylabel(y_label)  # Add custom y-axis label
    plt.grid(True, axis='x')  # Add grid only on the x-axis
    plt.show()


# Plot H0 barcode
plot_barcode(h0_diagram, "Barcode Plot for H0", "H0", "blue")

# Plot H1 barcode
plot_barcode(h1_diagram, "Barcode Plot for H1", "H1", "red")