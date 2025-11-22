#
# @lc app=leetcode id=3190 lang=python3
#
# [3190] Find Minimum Operations to Make All Elements Divisible by Three
#

# @lc code=start
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        #any numbers as at most one operation away 
        #from being divisible by 3
        result = 0
        
        for num in nums:
            if num % 3 != 0:
                result += 1
        
        return result
        
# @lc code=end

