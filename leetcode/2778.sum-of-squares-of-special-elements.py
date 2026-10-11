# @lc app=leetcode id=2778 slug=sum-of-squares-of-special-elements lang=python3
#
# [2778] Sum of Squares of Special Elements 
# Difficulty: Easy
# Tags: Array, Enumeration
# URL: https://leetcode.com/problems/sum-of-squares-of-special-elements/
#
# @lc code=start
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0

        for i in range(n):
            #print(i, n, (i+1) % n, result)
            if n % (i+1) == 0:
                result += nums[i] * nums[i]
        return result
            
        

# @lc code=end
