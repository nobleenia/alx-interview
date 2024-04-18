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
    if not (isinstance(boxes, list) and len(boxes) > 0):
        return False
    boxUnlocked = [False] * len(boxes)
    boxUnlocked[0] = True
    for i in range(len(boxes)):
        for j in range(len(boxes)):
            if boxUnlocked[j]:
                keys = boxes[j]
                for k in keys:
                    boxUnlocked[k] = True
    if sum(boxUnlocked) == len(boxes):
        return True
    return False