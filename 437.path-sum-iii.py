#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        Bacltracking,
        Any  given node can be considered the beginning of a path 
        a node is either at the start, inside, or end of the path
        Since negative numbers are allowed we can never terminate early 
        """
            
        def dfs(node):
            if not node:
                return 0
            return (
                path_from(node, 0)+
                dfs(node.left)+
                dfs(node.right)
            )
        
        def path_from(node, curr_sum):
            if not node:
                return 0
            curr_sum += node.val
            result = 0
            if curr_sum == targetSum:
                result += 1
            return result + path_from(node.left, curr_sum) + path_from(node.right, curr_sum)

        return dfs(root)
            
            
        
# @lc code=end

