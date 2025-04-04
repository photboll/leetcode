#
# @lc app=leetcode id=1123 lang=python3
#
# [1123] Lowest Common Ancestor of Deepest Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return (0, None)  # (depth, lca)

            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)

            if left_depth > right_depth:
                return (left_depth + 1, left_lca)
            elif right_depth > left_depth:
                return (right_depth + 1, right_lca)
            else:  # left_depth == right_depth
                return (left_depth + 1, node)

        return dfs(root)[1]

        
# @lc code=end

