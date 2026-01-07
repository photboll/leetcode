#
# @lc app=leetcode id=1339 lang=python3
#
# [1339] Maximum Product of Splitted Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
MOD = 10**9 + 7
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        """ 
        we need to know the total sum of the whole tree
        and then every p
        """
        all_sums = set()

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = left + right + root.val
            all_sums.add(res)
            return res
        
        total = dfs(root)
        result = 0
        for s in all_sums:
            val = s * (total - s)
            result = max(result, val)
        return result % MOD
            
            
        
# @lc code=end

