#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        #We do an inorder traversal and simply check at each step
        
        stack = []
        curr = root
        prev_val = float("inf")
        min_diff = float("inf")
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            min_diff = min(min_diff, abs(curr.val - prev_val))
            prev_val = curr.val
            
            curr = curr.right
        
        return min_diff

        
# @lc code=end

