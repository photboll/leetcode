#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
class SolutionV1:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def inorder_leaves(node, leaves):
            if node == None:
                return

            inorder_leaves(node.left, leaves)
            if node.left is None and node.right is None:
                #This is a leaf
                leaves.append(node.val)
            inorder_leaves(node.right, leaves)
        
        leaves1 = []
        inorder_leaves(root1, leaves1)
        leaves2 = []
        inorder_leaves(root2, leaves2)
        #print(leaves1)
        #print(leaves2)
        return leaves1 == leaves2
# @lc code=end

