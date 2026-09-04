# @lc app=leetcode id=3876 slug=construct-uniform-parity-array-ii lang=python3
#
# [3876] Construct Uniform Parity Array II
# Difficulty: Medium
# Tags: Array, Math
# URL: https://leetcode.com/problems/construct-uniform-parity-array-ii/
#
# @lc code=start
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = min((x for x in nums1 if x % 2), default=float("inf"))

        can_odd = all(x % 2 == 1 or (x > min_odd) for x in nums1)
        can_even = all(x % 2 == 0 or (x > min_odd) for x in nums1)

        return can_odd or can_even



        
                
            

        

# @lc code=end
