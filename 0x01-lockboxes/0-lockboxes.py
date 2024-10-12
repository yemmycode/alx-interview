#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''Checks if all boxes in the list can be unlocked.
    The first box is initially unlocked, and each box contains keys 
    (indices) to unlock other boxes.
    '''
    n = len(boxes)  
    seen_boxes = {0}  
    unseen_boxes = set(boxes[0]) - {0}  
    
    while unseen_boxes:  
        boxIdx = unseen_boxes.pop()  
        if boxIdx <= 0 or boxIdx >= n:
            continue  
        if boxIdx not in seen_boxes:  
            unseen_boxes |= set(boxes[boxIdx])  
            seen_boxes.add(boxIdx)  
    
    return len(seen_boxes) == n   
