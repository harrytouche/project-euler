"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

import numpy as np

side = 2

# create grid
grid = np.zeros((side,side), dtype=int)

# loop through grid from top right
for i in range(side):
    
    grid_x = i
    grid_y = side-i
            
    grid[grid_x, grid_y] = grid[grid_x-1, grid_y] + grid[grid_x, grid_y-1]
    
print(grid[-1,-1])