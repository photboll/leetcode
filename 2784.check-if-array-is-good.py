#
# @lc app=leetcode id=2784 lang=python3
#
# [2784] Check if Array is Good
#

# @lc code=start
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) -1
        nums.sort()
        for i in range(n):
            if nums[i] != i + 1:
                return False
        return nums[n] == n

            
        
# @lc code=end

