# @lc app=leetcode id=1569 slug=number-of-ways-to-reorder-array-to-get-same-bst lang=python3
#
# [1569] Number of Ways to Reorder Array to Get Same BST
# Difficulty: Hard
# Tags: Array, Math, Divide and Conquer, Dynamic Programming, Tree, Union-Find, Binary Search Tree, Memoization, Combinatorics, Binary Tree, Fermat's Little Theorem
# URL: https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/
#
# @lc code=start
from math import comb
MOD = pow(10, 9) + 7
class Solution:
    def numOfWays(self, nums: list[int]) -> int:

        def dfs(arr):
            m = len(arr)

            if m < 3:
                return 1
            
            left_nodes = [a for a in arr if a < arr[0]]
            right_nodes = [a for a in arr if a > arr[0]]

            return (dfs(left_nodes) * dfs(right_nodes) *comb(m-1, len(left_nodes)) ) % MOD
        return (dfs(nums) -1) % MOD
        

# @lc code=end
