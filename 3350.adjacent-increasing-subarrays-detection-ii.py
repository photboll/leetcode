#
# @lc app=leetcode id=3350 lang=python3
#
# [3350] Adjacent Increasing Subarrays Detection II
#

# @lc code=start
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        
        count = 1
        prev_count = 0
        result = 0
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                count += 1
            else:
                prev_count = count
                count = 1
            result = max(result, min(prev_count, count))
            #we can always split the current conut into two adjacent increasing subarrays
            result = max(result, count//2)

        return result 
        
# @lc code=end

