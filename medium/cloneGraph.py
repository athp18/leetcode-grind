# revisiting old problems

class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        hashmap = {} # hashmap to store key, val pairs and for O(1) lookup
        if not node: # edge case: no node
            return None
        
        def dfs(node): # recursive function
            if node in hashmap: # we've iterated through all nodes, thus can return the hashmap[node]
                return hashmap[node]
            
            temp = Node(node.val) # starting point
            hashmap[node] = temp # add starting point to hashmap

            for n in node.neighbors: # iterate over the node's neighbors
                temp.neighbors.append(dfs(n)) # append the result to our temp var
            return temp
        
        return dfs(node) 
