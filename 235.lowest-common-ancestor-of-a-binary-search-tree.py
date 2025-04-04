#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root       
        
        #How do they three nods values relate to each other
        if root.val > p.val and root.val >q.val:
            #Root value is larger than both p and q
            #lca must be in the left subtree
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val :
            #Root value is less than both p and q
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            #One is in the left subtree and the other is in the right
            #root is the LCA
            return root
            
# @lc code=end

