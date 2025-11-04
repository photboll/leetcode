#
# @lc app=leetcode id=3318 lang=python3
#
# [3318] Find X-Sum of All K-Long Subarrays I
#

# @lc code=start
from collections import Counter

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def x_sum(freqs):
            topX = sorted(freqs.items() ,key=lambda cnt: (-cnt[1], -cnt[0]))[:x]
            return sum(key * val for key, val in topX)
        
        n = len(nums)
        result = []
        for i in range(n-k+1):
            xSum = x_sum(Counter(nums[i:i+k]))
            result.append(xSum)
        return result
        
# @lc code=end

