#
# @lc app=leetcode id=3542 lang=python3
#
# [3542] Minimum Operations to Convert All Elements to Zero
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        s = []
        res = 0
        for a in nums:
            while s and s[-1] > a:
                s.pop()
            if a == 0:
                continue
            if not s or s[-1] < a:
                res += 1
                s.append(a)
        return res
        
# @lc code=end

