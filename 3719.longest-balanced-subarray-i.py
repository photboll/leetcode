#
# @lc app=leetcode id=3719 lang=python3
#
# [3719] Longest Balanced Subarray I
#

# @lc code=start
from collections import Counter

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)

        for l in range(n):
            seen, B = set(), 0
            for r in range(l, n):
                x = nums[r]
                if x not in seen:
                    seen.add(x)
                    B += 1 if (x % 2) == 0 else -1
                if B == 0:
                    result = max(result, r-l+1)
        return result

            

        
# @lc code=end

