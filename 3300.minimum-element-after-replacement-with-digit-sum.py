#
# @lc app=leetcode id=3300 lang=python3
#
# [3300] Minimum Element After Replacement With Digit Sum
#

# @lc code=start
class Solution:
    def minElement(self, nums: List[int]) -> int:
        def digitsum(x):
            s = 0
            while x > 0:
                x, rem = divmod(x, 10)
                s += rem
            return s
        
        res = float("inf")
        for num in nums:
            res = min(res, 
                      digitsum(num))
        
        return res

        


        
# @lc code=end

