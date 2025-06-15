#
# @lc app=leetcode id=3357 lang=python3
#
# [3357] Minimize the Maximum Adjacent Element Difference
#

# @lc code=start
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        """
        We can only affect the absolute difference of numbers that are directly adjacent to a -1
        we want to minimize a maximum value which hints at using a binary search approch on the solution space.
        What range is our solution space? the absolute minimal possible absolute difference
        is the min difference of any two neighbors. in ex 1 the 10 and 8 gives a absolute difference of 2
        so any solution needs to be larger than or equal to two
        The interior of any substring of -1 should be filled uniformly. no it is not always possible to do this,
        we can only select two postiive integers x and y
        
        Maybe it helps to solve a similar alternative problem.
        What happens if we are allowed to choose as many digits as we want?
        What happens if we consider it for a fixed pair of digits?
        """
        
# @lc code=end


