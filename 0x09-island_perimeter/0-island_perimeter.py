#!/usr/bin/python3
"""Implement Island Perimeter algorithm"""


def expand_grid(grid):
    """Expand island with more waters"""
    land_size = len(grid[0]) + 2

    grid.insert(0, [0] * land_size)
    grid.append([0] * land_size)

    for row in grid[1:-1]:
        row.insert(0, 0)
        row.append(0)

    return grid


def island_perimeter(grid: list):
    """Returns the perimeter of the island described in grid"""

    perimeter = 0
    grid = expand_grid(grid)

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            if grid[i][j]:
                if grid[i - 1][j] == 0:
                    perimeter += 1
                if grid[i][j - 1] == 0:
                    perimeter += 1
                if grid[i + 1][j] == 0:
                    perimeter += 1
                if grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
