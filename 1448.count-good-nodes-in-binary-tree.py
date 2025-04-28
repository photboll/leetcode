#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]
        
        def recur(node, max_val=float("-inf")):
            if not node:
                return 

            if node.val >= max_val:
                #This node is good
                count[0] += 1
                max_val = node.val
            
            recur(node.left, max_val)
            recur(node.right, max_val)
        
        recur(root)
        return count[0]
        
# @lc code=end

