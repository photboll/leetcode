# @lc app=leetcode id=3727 slug=maximum-alternating-sum-of-squares lang=python3
#
# [3727] Maximum Alternating Sum of Squares
# Difficulty: Medium
# Tags: Array, Greedy, Sorting
# URL: https://leetcode.com/problems/maximum-alternating-sum-of-squares/
#
# @lc code=start
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        """
        Maximumes alternating sum 
        every entry is squared so we only care about the absolute value of each one
        
        maximum is achieved when those with positive sign have the maximum value possible 
        and those with negative value 

        sort the values 
        and then let the first half be the positive ones and the second half the negative ones
        """
        nums = [v*v for v in nums]
        nums.sort(reverse=True)

        # bias mid so that odd length arrays asigns the middle element to the first half
        mid = (len(nums) + 1) // 2
        result = sum(nums[:mid])
        result -= sum(nums[mid:])
        return result 
        


        

        

# @lc code=end
