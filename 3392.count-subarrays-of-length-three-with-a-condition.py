#
# @lc app=leetcode id=3392 lang=python3
#
# [3392] Count Subarrays of Length Three With a Condition
#

# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        
        for i in range(1, n-1):
            if nums[i] == 2 *(nums[i-1] + nums[i+1]):
                count += 1
        return count 
                
        
# @lc code=end

