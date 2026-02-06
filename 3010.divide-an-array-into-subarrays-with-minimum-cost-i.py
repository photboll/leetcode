#
# @lc app=leetcode id=3010 lang=python3
#
# [3010] Divide an Array Into Subarrays With Minimum Cost I
#

# @lc code=start
from heapq import nsmallest
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        """
        Equivalent to finding the three smallest elements
        """
        return nums[0] + sum(nsmallest(2,nums[1:]))
        
# @lc code=end

