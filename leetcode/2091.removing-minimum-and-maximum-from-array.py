# @lc app=leetcode id=2091 slug=removing-minimum-and-maximum-from-array lang=python3
#
# [2091] Removing Minimum and Maximum From Array
# Difficulty: Medium
# Tags: Array, Greedy
# URL: https://leetcode.com/problems/removing-minimum-and-maximum-from-array/
#
# @lc code=start
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        """integers in nums are distinct"""
        n = len(nums)
        mx =  float("-inf")
        mxi = -1
        mn =  float("inf")
        mni = -1

        for i, num in enumerate(nums):
            if num > mx:
                mx = num
                mxi = i
            if num < mn:
                mn = num
                mni = i
        
        # 1. Remove both from the front
        result = max(mxi, mni) + 1

        # 2. Remove both from the back
        result = min(result, n - min(mxi, mni))

        # 3. Max from front, min from back
        result = min(result, mxi + 1 + n - mni)

        # 4. Min from front, max from back
        result = min(result, mni + 1 + n - mxi)

        return result
        

# @lc code=end
