import numpy as np
import matplotlib.pyplot as plt

def initialize_grid(live_cells, size=30):
    grid = np.zeros((size, size), dtype=int)
    for cell in live_cells:
        grid[cell] = 1
    return grid

def get_neighbours(x, y, grid):
    neighbours = [
        (x-1, y-1), (x-1, y), (x-1, y+1),
        (x, y-1),           (x, y+1),
        (x+1, y-1), (x+1, y), (x+1, y+1)
    ]
    return [grid[i, j] for i, j in neighbours if 0 <= i < grid.shape[0] and 0 <= j < grid.shape[1]]

def update_grid(grid):
    new_grid = grid.copy()
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            neighbours = get_neighbours(i, j, grid)
            alive = neighbours.count(1)
            if grid[i, j] == 1:
                if alive < 2 or alive > 3:
                    new_grid[i, j] = 0
            else:
                if alive == 3:
                    new_grid[i, j] = 1
    return new_grid

def run_simulation(live_cells, steps=100):
    grid = initialize_grid(live_cells)
    for step in range(steps):
        new_grid = update_grid(grid)
        if np.array_equal(grid, new_grid):
            break
        grid = new_grid
    return grid, step

# Example for question 4
live_cells_q4 = [(14, 15), (15, 15), (16, 15), (15, 14), (16, 16), (14, 16), (15, 17)]
resulting_grid_q4, steps_q4 = run_simulation(live_cells_q4)
print("Steps to steady state:", steps_q4)

# To visualize the grid
plt.imshow(resulting_grid_q4, cmap='binary')
plt.show()

# Similar code can be used to simulate and answer questions 5, 6, and 7.
