#
# @lc app=leetcode id=3314 lang=python3
#
# [3314] Construct the Minimum Bitwise Array I
#

# @lc code=start
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            res = -1
            d = 1
            while (nums[i] & d) != 0:
                res = nums[i] -d 
                d <<= 1
            nums[i] = res
        return nums
        
# @lc code=end

