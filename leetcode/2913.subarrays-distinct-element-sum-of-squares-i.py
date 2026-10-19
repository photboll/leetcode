# @lc app=leetcode id=2913 slug=subarrays-distinct-element-sum-of-squares-i lang=python3
#
# [2913] Subarrays Distinct Element Sum of Squares I
# Difficulty: Easy
# Tags: Array, Hash Table, Binary Indexed Tree, Segment Tree
# URL: https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/
#
# @lc code=start

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        s = set()

        for l in range(n):
            s.clear()
            for r in range(l, n):
                s.add(nums[r])
                result += len(s) * len(s)
        return result


            
        

# @lc code=end
