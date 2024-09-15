from collections import deque


def findMaxValueOfEquation(points, k):
    deque = deque()
    MAX = float('-inf')
    
    for xj, yj in points:
        while deque and xj - points[deque[0]][0] > k:
            deque.popleft()
        if deque:
            MAX = max(MAX, points[deque[0]][1] - points[deque[0]][0] + yj + xj)
        
        #remove all points from the deque where yi - xi is smaller than yj - xj
        while deque and points[deque[-1]][1] - points[deque[-1]][0] <= yj - xj:
            deque.pop()
        deque.append(len(points) - len(deque) - 1)
    
    return MAX
