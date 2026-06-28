#
# @lc app=leetcode id=1846 lang=python3
#
# [1846] Maximum Element After Decreasing and Rearranging
#

# @lc code=start
from heapq import heapify, heappop, heappush
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        heapify(arr)
        curr = 1
        while arr:
            num = heappop(arr)
            if num >= curr:
                curr += 1
        return curr -1
        






        
# @lc code=end

