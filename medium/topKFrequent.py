import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        hashlist = (sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
        reslst = [item[0] for item in hashlist[:k]]
        return reslst
        # well that's the brute force solution. it has O(n log n) time complexity

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: # more efficient
        hashmap = {} # use a hashmap
        for num in nums: # find frequencies
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        heap = [] # create a heap as a list -- although its a python list, it works well here an reduces the operation

        for key, val in hashmap.items(): # iterate through the hashmap
            if len(heap) < k: # basically, we make sure that the heap only has k elements. so we're using a min heap here. basically, a min heap has the property of being a binary tree where the parent node is always smaller than the child node
                heapq.heappush(heap, (val, key)) # push a tuple (val, key) -- val here is the frequency which is what we want to "sort"
            else:
                heapq.heappushpop(heap, (val, key)) # now here's the cool thing. if the length of our list is at k, we pop the first element from the heap and append a new one. keep in mind that since our heap is "sorted" with the highest frequency elems at the back, this effectively removes the lowest frequency elements
        
        return [h[1] for h in heap] # the vals are the 1st element so we return a list of that. our heap has length k so we chillin

