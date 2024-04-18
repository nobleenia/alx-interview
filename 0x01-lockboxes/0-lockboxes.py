#!/usr/bin/python3
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
    # Start with box 0 unlocked and its keys available
    unlocked = set([0])
    queue = [0]  # Use a list as a queue for BFS

    while queue:
        # Get the next box to process
        current_box = queue.pop(0)
        
        # Iterate over each key in the current box
        for key in boxes[current_box]:
            # If the key corresponds to a
            # box we haven't unlocked yet
            if key not in unlocked and key < len(boxes):
                unlocked.add(key) # Mark box as unlocked
                queue.append(key) # Add box to the queue

    # If the number of unlocked boxes equals
    # the number of boxes, we've unlocked all of them
    return len(unlocked) == len(boxes)

if __name__ == "__main__":
    canUnlockAll(boxes)
