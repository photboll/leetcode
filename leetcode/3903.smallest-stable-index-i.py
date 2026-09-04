# @lc app=leetcode id=3903 slug=smallest-stable-index-i lang=python3
#
# [3903] Smallest Stable Index I
# Difficulty: Easy
# Tags: Array, Prefix Sum
# URL: https://leetcode.com/problems/smallest-stable-index-i/
#
# @lc code=start
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        mn = nums[-1]

        mins = [float("inf")] * n
        for i in range(n-1, -1, -1):
            if nums[i] < mn:
                mn = nums[i]
            mins[i] = mn
        
        print(mins)
        
        mx = nums[0]
        for i in range(n):
            if nums[i] > mx:
                mx = nums[i]

            score = mx - mins[i]
            if score <= k:
                return i
        return -1
            
        

# @lc code=end
