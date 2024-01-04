#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(levels):
    """Implementation of pascal's triangle algorithm"""
    if levels <= 0:
        return []

    pascal_list = [[1]]

    for row in range(1, levels):
        previous_level = pascal_list[row - 1]
        current_level = [1] + [previous_level[i] + previous_level[i + 1]
                               for i in range(len(previous_level) - 1)] + [1]

        pascal_list.append(current_level)

    return pascal_list
