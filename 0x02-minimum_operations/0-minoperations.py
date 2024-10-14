#!/usr/bin/python3
'''Challenge: Calculate the minimum operations.
'''

def minOperations(n):
    '''Determines the minimum number of operations required
    to get exactly n 'H' characters.
    '''
    if not isinstance(n, int):
        return 0
    ops_count = 0
    clipboard = 0
    current = 1

    while current < n:
        if clipboard == 0:
            # Initial copy and paste operation
            clipboard = current
            current += clipboard
            ops_count += 2
        elif (n - current) > 0 and (n - current) % current == 0:
            # Perform copy and paste when remainder is divisible by current
            clipboard = current
            current += clipboard
            ops_count += 2
        else:
            # Just paste the current clipboard value
            current += clipboard
            ops_count += 1

    return ops_count

