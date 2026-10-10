# @lc app=leetcode id=2333 slug=minimum-sum-of-squared-difference lang=python3
#
# [2333] Minimum Sum of Squared Difference
# Difficulty: Medium
# Tags: Array, Binary Search, Greedy, Sorting, Heap (Priority Queue)
# URL: https://leetcode.com/problems/minimum-sum-of-squared-difference/
#
# @lc code=start
from heapq import heappush, heappop, heapify
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]
        diffs.sort(reverse=True)
        diffs.append(0)
        k = k1 + k2


        for i in range(n):
            width = i + 1
            cost = (diffs[i] - diffs[i+1]) * width

            if cost <= k:
                k -= cost
            else:
                full, rem = divmod(k, width)
                level = diffs[i] - full
                top = level * level * (width - rem) + (level -1)**2 *rem
                return top + sum(d*d for d in diffs[width:n])
            
        
        return 0


            
        

# @lc code=end
