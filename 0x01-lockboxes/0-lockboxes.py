#!/usr/bin/python3
"""Lockboxes Algorithm"""


def canUnlockAll(boxes):
    if len(boxes) == 1:
        return True

    visited = {0}
    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key not in visited and key < len(boxes):
                visited.add(key)
                stack.append(key)

    return len(visited) == len(boxes)


# TODO: Refactor the bug in code below, it causes by `last_box` variable


def can_unlock_all(boxes):
    """function to unlock all boxes"""
    if len(boxes) == 1:
        return True

    visited = [0]
    opened = [True] + [False] * (len(boxes) - 1)

    open_boxes(boxes, visited, opened)
    return all(opened)


def open_boxes(boxes, visited, opened, last_box=-1):
    """function that tries to open all boxes"""
    if len(visited) == len(boxes):
        return

    for key in boxes[visited[last_box]]:
        if key in visited:
            continue
        visited.append(key)
        opened[key] = True

    if len(boxes[visited[last_box]]):
        last_box -= 1
    return open_boxes(boxes, visited, opened, last_box)
