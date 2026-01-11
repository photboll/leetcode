#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """ 
        Dp approach. can we extend the square case to rectangle?
        that will probably be very messy 
        Base case: 1xn and mx1
        if current is a one extend the previos with one else 
        n 
        
        """
        
# @lc code=end

