#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((root, 1)) # (node, level)
        argmax = 0
        max_val = float("-inf")
        curr_sum = 0
        curr_level = 1
        while q:
            curr_node, level = q.popleft()
            if level == curr_level:
                curr_sum += curr_node.val
            else:
                if curr_sum > max_val:
                    max_val = curr_sum
                    argmax = curr_level
                curr_sum = curr_node.val
                curr_level = level
            
            if curr_node.left:
                q.append((curr_node.left, level+1))
            
            if curr_node.right:
                q.append((curr_node.right, level+1))
        
        #Remmber to check if the last level beats the max
        if curr_node:
            if curr_sum > max_val:
                max_val = curr_sum
                argmax = curr_level
            curr_sum = curr_node.val
            curr_level = level
            
        return argmax

        
# @lc code=end

