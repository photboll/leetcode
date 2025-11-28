#
# @lc app=leetcode id=2872 lang=python3
#
# [2872] Maximum Number of K-Divisible Components
#

# @lc code=start
from collections import defaultdict 
class ListNode:
    def __init__(self, val=0, next=None, n_children=0):
        self.val = val
        self.next = next
        self.n_children = n_children

def build_tree(edges, values):
    neighbors = defaultdict(list)
    for u, v in edges:
        neighbors[u].append(v)
        neighbors[v].append(u)
    
    
    nodes = [ListNode(val=values[i]) for i in range(len(values))]

    leaves = []
    visited = set()
    stack = [0]
    visited.add(stack[0])
    while stack:
        curr = stack.pop()

        is_leaf = True
        for neigh in neighbors[curr]:
            if neigh not in visited:
                #curr have atleast one child so it cant be a leaf
                is_leaf = False
                nodes[neigh].next = nodes[curr]#make it point to the parent 
                nodes[curr].n_children += 1
                stack.append(neigh)
                visited.add(neigh)
        
        if is_leaf:
            leaves.append(nodes[curr])   
    
    return nodes[0], leaves

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        root, leaves,  = build_tree(edges, values)

        result = 0 
        while len(leaves) > 0:
            #Keep merging each leaf with its parent until the value is divisible by k
            #then we have a connected component which fulfills the criteria 
            leaf = leaves.pop()
            if leaf.val % k == 0:
                # Cut the edge. we have our connected component
                result += 1
            else:
                # merge leaf with parent 
                if leaf.next:
                    leaf.next.val += leaf.val
                
            #did the parent become a leaf after the merge?
            parent = leaf.next
            if parent:
                parent.n_children -= 1
                if parent.n_children == 0:
                    leaves.append(parent)
                
        return result
            

                    
                
            
        
        
                

        



        
# @lc code=end

