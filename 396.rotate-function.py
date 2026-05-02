#
# @lc app=leetcode id=396 lang=python3
#
# [396] Rotate Function
#

# @lc code=start
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        tot = 0
        for i, num in enumerate(nums):
            tot += i * num

        res = float("-inf")
        for i in range(n-1, -1,-1 ):
            tot -= nums[i] * (n-1)
            tot += s - nums[i]
            res = max(res, tot)
            

        #print(s, tot, nums)
        return res
        
# @lc code=end

    