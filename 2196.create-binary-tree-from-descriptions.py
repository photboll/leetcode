#
# @lc app=leetcode id=2196 lang=python3
#
# [2196] Create Binary Tree From Descriptions
#

# @lc code=start
# Definition for a binary tree node.
#class TreeNode:
#    def __init__(self, val=0, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right
#    
#    def __str__(self):
#        return str(self.val)

from collections import defaultdict
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        #prep datastructures to find relations efficiently
        val2node = {}
        val2children = defaultdict(list)
        for parent, child, isLeft in descriptions:
            node = TreeNode(val=child)
            val2children[parent].append((child, isLeft))
            val2node[child] = node

        #find root
        #the root must have never been listed as a parent
        for parent, child, isLeft in descriptions:
            if parent not in val2node:
                root = TreeNode(val=parent)
            
        
        def dfs(node):
            if node == None:
                return 
            
            for child, isLeft in val2children[node.val]:
                if isLeft:
                    node.left = val2node[child]
                    dfs(node.left)
                else:
                    node.right = val2node[child]
                    dfs(node.right)
        
        dfs(root)
        #print(val2children)
        #print(val2node)

        return root





        
# @lc code=end

