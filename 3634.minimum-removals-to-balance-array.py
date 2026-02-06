#
# @lc app=leetcode id=3634 lang=python3
#
# [3634] Minimum Removals to Balance Array
#

# @lc code=start
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        r = 0
        for l in range(n):
            while r < n and nums[r] <= nums[l] * k:
                r += 1
            res = min(res, n - (r-l))
        return res
            

            

            

        
# @lc code=end

