#
# @lc app=leetcode id=453 lang=python3
#
# [453] Minimum Moves to Equal Array Elements
#

# @lc code=start
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        """
        we can only increment
        we have to increment n-1 in each operation
        start with incrementing all except the largest num
        maybe we can flip it and do the opposite, decrease one of the nums at each step until
        all numbers are equal 
        """
        mini = min(nums)
        result = 0
        for num in nums:
            result += num - mini
        return result 

        
# @lc code=end

