"""
Given an integer array, perform operations by selecting 2 elements from the array, 
sum them up and delete those two elements from the array and 
add the new sum to the array. Return the final sum.
"""

import heapq

def sum_elems(arr):
    if not arr:
        return 0
    heapq.heapify(arr)
    while len(arr) > 1:
        i = heapq.heappop(arr)
        j = heapq.heappop(arr)

        new = i + j
        heapq.heappush(arr, new)
    return arr[0]
