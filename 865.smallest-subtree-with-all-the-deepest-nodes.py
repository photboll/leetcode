#
# @lc app=leetcode id=865 lang=python3
#
# [865] Smallest Subtree with all the Deepest Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return None, 0
            l_node, l_depth = dfs(node.left)
            r_node, r_depth = dfs(node.right)
            if l_depth > r_depth :
                return l_node, l_depth + 1
            if r_depth > l_depth:
                return r_node, r_depth + 1
            return node, l_depth + 1
        
        lca, depth = dfs(root)
        return lca



        
# @lc code=end

