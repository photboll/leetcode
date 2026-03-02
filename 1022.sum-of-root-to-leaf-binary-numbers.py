#
# @lc app=leetcode id=1022 lang=python3
#
# [1022] Sum of Root To Leaf Binary Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, n):
            if not node: return

            n = 2* n + node.val
            if not node.left and not node.right:
                self.ans+= n
                return
            dfs(node.left, n)
            dfs(node.right, n)

            return
        self.res = 0
        dfs(root)
        return self.res
        
        
# @lc code=end

