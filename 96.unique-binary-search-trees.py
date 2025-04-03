#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}
        
        def dp(num_nodes):
            if num_nodes <= 1:
                return 1
            if num_nodes in memo:
                return memo[num_nodes]
            #Left subtree can have anything from 0 to num_nodes-1
            #Right subtree will have the remaining nodes
            num_BSTs = 0
            for left_subtree_size in range(num_nodes):
                right_subtree_size = num_nodes-1 - left_subtree_size
                num_BSTs += dp(left_subtree_size) * dp(right_subtree_size)
                #print(num_nodes, num_BSTs, left_subtree_size, right_subtree_size) 
            memo[num_nodes] = num_BSTs
            return num_BSTs
        return  dp(n)
# @lc code=end

