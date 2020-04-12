"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

import numpy as np

grid_size = 20

# create grid
side = grid_size + 1
grid = np.zeros((side, side), dtype=int)
grid.fill(1)

# loop through grid from top right
for i in range(side * 2):

    # print("i = {}".format(i))

    for j in range(i + 1):
        grid_x = j
        grid_y = i - j

        """
        print("{} / {}".format(j, i))
        print("grid_x = {}".format(grid_x))
        print("grid_y = {}".format(grid_y))
        input("Press enter to proceed")
        """

        if grid_x != 0 and grid_y != 0 and grid_x < side and grid_y < side:
            grid[grid_x, grid_y] = grid[grid_x - 1, grid_y] + grid[grid_x, grid_y - 1]


# print(grid)
print(grid[-1, -1])
