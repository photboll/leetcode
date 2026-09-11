# @lc app=leetcode id=2265 slug=count-nodes-equal-to-average-of-subtree lang=python3
#
# [2265] Count Nodes Equal to Average of Subtree
# Difficulty: Medium
# Tags: Tree, Depth-First Search, Binary Tree
# URL: https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/
#
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def recur(node, result):
            #return sum, count
            if node == None:
                return 0, 0
            
            sum_l, cnt_l = recur(node.left, result)
            sum_r, cnt_r = recur(node.right, result)

            cnt_tot = cnt_l + cnt_r + 1

            if node.val == (sum_l + sum_r + node.val) // cnt_tot:
                result[0] += 1

            
            return node.val + sum_l + sum_r, cnt_r + cnt_l + 1
        
        result = [0]
        recur(root, result)
        
        return result[0]

# @lc code=end
