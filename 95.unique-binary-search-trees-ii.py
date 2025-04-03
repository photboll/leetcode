#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}
        def dp(start, end)-> List[Optional[TreeNode]]:
            if start > end:
                return [None]
        
            if ( start, end) in memo:
                return memo[(start, end)]
            
            all_trees = []
            for root_val in range(start, end+1):
                left_trees = dp(start, root_val -1)
                right_trees = dp(root_val +1, end)
                
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        all_trees.append(root)
            memo[(start, end)] = all_trees
            return all_trees
        return dp(1, n)
        
        
# @lc code=end

