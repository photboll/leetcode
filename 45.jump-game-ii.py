#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0 #Total number of jumps so far
        current_end = 0 #End of the current considered jump
        farthest = 0 #fasrthest jump seen so far
        for i in range(len(nums)-1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                #We need another jump
                jumps += 1
                current_end = farthest
        return jumps
            
class SolutionV1:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums) 
        def dp(i) -> int:
            if i >= n -1:
                return 0
            
            if i in memo:
                return memo[i]
            
            min_jumps = float("inf")
            for j in range(1, nums[i]+1):
                min_jumps = min(min_jumps, dp(i + j) + 1)
            
            memo[i] = min_jumps
            return min_jumps
        return dp(0)
            
            
        
# @lc code=end

