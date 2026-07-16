#
# @lc app=leetcode id=3867 lang=python3
#
# [3867] Sum of GCD of Formed Pairs
#

# @lc code=start
from math import gcd 

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefix_grid = [0] * n

        mx = nums[0]
        for i in range(n):
            mx = max(mx, nums[i])
            prefix_grid[i] = gcd(nums[i], mx)
        
        prefix_grid.sort()
        l = 0
        r = n-1
        res = 0
        while l < r:
            res += gcd(prefix_grid[l], prefix_grid[r])
            l += 1
            r -= 1
        return res 
            
        
# @lc code=end

