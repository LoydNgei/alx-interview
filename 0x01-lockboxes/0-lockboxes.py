#!/usr/bin/python3
""" Write a method that determines if all the boxes can be opened """


def canUnlockAll(boxes):
    if len(boxes) == 0:
        return True

    keys = set(boxes[0])  # Keys obtained from the first box
    checked = set([0])  # Set to track the visited boxes

    # Perform BFS
    while keys:
        new_keys = set()

        # Iterate through the keys obtained so far
        for key in keys:
            # Check if the key unlocks a new box
            if key < len(boxes) and key not in checked:
                checked.add(key)
                # Add the keys in the newly opened box
                new_keys.update(boxes[key])

        keys = new_keys  # Update the keys obtained in this iteration

    # Check if all boxes have been visited
    return len(checked) == len(boxes)
