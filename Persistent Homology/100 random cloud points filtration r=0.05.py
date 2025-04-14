# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 20:15:43 2025

@author: addf188
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance_matrix

# Set random seed and generate 2D points
points = np.random.rand(100, 2)
np.random.seed(30)

# Set radius
r = 0.05

# Compute the distances between different points
dists = distance_matrix(points, points)
n = 100

# Create diagram
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_title("r = 0.05")

for point in points:
    # First, we plot the scatter diagram of the 100 points
    ax.scatter(*point, color='black', zorder=4) # zorder set to 4 to ensure that it will appear at the top layer out of the 4 layers
    # Secondly, we add circles around each point, we've set the colour as black and alpha as 0.1 so we would be able to see the overlapping and other features.
    circle = plt.Circle(point, radius=0.05, color='black', alpha=0.1, zorder=1) #zorder=1 so it would be the bottom layer
    # We add the circles to the plot
    ax.add_patch(circle)

# Here we determined that if distances between 2 points is less than or equal to 2r, it means that two circles touches and an edge is formed
Edge_form = dists <= 2 * r

for i in range(n):
    # Here we have used i+1 so that i does not equal to i, only check for points that are not themselves
    for j in range(i + 1, n):
        # We check if the two circles touches each other, only proceed if it is true
        if Edge_form[i,j]:
            # Add edges
            ax.plot([points[i, 0], points[j, 0]], #column 0 of points would be our x values
                    [points[i, 1], points[j, 1]], # column 1 of points would be our y values
                    color='purple', linewidth=1, zorder=3) # zorder= 3 so that it's one layer under the points

# Now we are going to fill in all triangles representing a loop
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if Edge_form[i,j] and Edge_form[j,k] and Edge_form[k,i]: # Checking if the three points creates a triangle, they do if there's an edges connecting any two points
                triangle = [points[i], points[j], points[k]] 
                poly = plt.Polygon(triangle, color='violet', alpha=0.5, zorder=2)
                ax.add_patch(poly)

plt.show()