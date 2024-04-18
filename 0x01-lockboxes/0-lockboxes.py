#!/usr/bin/env python3
"""
This module contains a function that determines
if all boxes in a list can be opened.
Each box may contain keys to other boxes.
The function uses a breadth-first search algorithm
to unlock all accessible boxes starting from box 0,
which is initially unlocked.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list of lists of int): A list where
        each element is a list of integers,
        representing the keys in each box.

    Returns:
        bool: True if all boxes can be unlocked,
        otherwise False.
    """
    if (type(boxes) is not list):
        return False

    if (len(boxes) == 0):
        return False

    keys = [0]
    for i in keys:
        for j in boxes[i]:
            if j not in keys and j != i and j < len(boxes) and j != 0:
                keys.append(j)
    if len(keys) == len(boxes):
        return True
    else:
        return False
