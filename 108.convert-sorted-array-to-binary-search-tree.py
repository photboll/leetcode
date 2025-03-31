#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        if n == 0:
            return None
        root_i = n // 2
        root = TreeNode(val=nums[root_i])
        root.left = self.sortedArrayToBST(nums[:root_i])
        root.right = self.sortedArrayToBST(nums[root_i + 1:])
        
        return root
        
        
# @lc code=end

