#
# @lc app=leetcode id=1382 lang=python3
#
# [1382] Balance a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        inorder = []
        
        def inorder_traversal(root):
            if not root:
                return 
            
            inorder_traversal(root.left)
            inorder.append(root.val)
            inorder_traversal(root.right)
        
        def create_balanced(vals, start, end):
            if start > end:
                return 
            
            mid = start+ (end- start) // 2
            
            left_tree = self.create_balanced(vals, start, mid+1)
            right_tree = self.create_balanced(vals, mid+1, end)

            root = TreeNode(vals[mid], left_tree, right_tree)
            return root
        
        return create_balanced(inorder, 0, len(inorder)-1)
            

    
        
# @lc code=end

