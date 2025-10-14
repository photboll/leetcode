#
# @lc app=leetcode id=3349 lang=python3
#
# [3349] Adjacent Increasing Subarrays Detection I
#

# @lc code=start
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        inc = 1
        prevInc = 0
        max_length = 0 
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc += 1
            else:
                prevInc = inc
                inc =1
            max_length = max(max_length, max(inc >> 1, min(prevInc, inc)))
            if max_length >= k:
                return True

        return False
        
# @lc code=end

