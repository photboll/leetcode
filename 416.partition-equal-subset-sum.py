#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #if the sum of nums is odd then it is impossible
        #Otherwise we need to find a subset of the array that is equal to sum // 2 
        #Knapsack dp 
        tot = sum(nums)
        if tot % 2 == 1:
            return False
        
        target = tot // 2
        #dp[i] is true if it is possible to create a sum of i with the subsets 
        dp = [False] *(target +1)
        dp[0] = True
        for num in nums:
            for i in range(target, num-1, -1):
                dp[i] |= dp[i-num]
        #print(dp)
        return dp[-1]
# @lc code=end

