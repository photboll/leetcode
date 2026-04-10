#
# @lc app=leetcode id=3741 lang=python3
#
# [3741] Minimum Distance Between Three Equal Elements II
#

# @lc code=start
from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        result = float("inf")
        val2is = defaultdict(list)

        for i, val in enumerate(nums):
            val2is[val].append(i)
        
        for indices in val2is.values():
            #there must be at least three indices for a good tuple to exist
            for i in range(2, len(indices)):
                distance = 2 * (indices[i] - indices[i-2])
                result = min(result, distance)
                
            



        return result if result != float("inf") else -1

        
# @lc code=end

