#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        node_copies = {node:Node(node.val)}#Maps the original node to the copies 
        stack = [node]#holds the original nodes
        while stack:
            #print(f"{[n.val for n in stack]}")
            curr_node = stack.pop()
            curr_copy = node_copies[curr_node]
            for next_node in curr_node.neighbors:
                #Create the neighboring copy if it doe not exist yet 
                if next_node not in node_copies:
                    node_copies[next_node] = Node(next_node.val)
                    stack.append(next_node)
        
                #Set the copied neighbor to be a neigbor of the current copy
                next_copy = node_copies[next_node]
                curr_copy.neighbors.append(next_copy)

            
        return node_copies[node]
        
        
# @lc code=end

