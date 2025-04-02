#
# @lc app=leetcode id=2012 lang=python3
#
# [2012] Sum of Beauty in the Array
#

# @lc code=start
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        prefixMax = [nums[0]] * n
        suffixMin = [nums[-1]]* n
        for i in range(1, n):
            prefixMax[i] = max(prefixMax[i -1], nums[i])
        for i in range(n - 2, -1, -1):
            suffixMin[i] = min(suffixMin[i+1], nums[i])

        beautySum = 0   
        for i in range(1, n-1):
            #Determine beuty of current num
            if prefixMax[i-1] < nums[i] < suffixMin[i+1]:
                beautySum += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                beautySum += 1
        
        return beautySum
            
# @lc code=end

