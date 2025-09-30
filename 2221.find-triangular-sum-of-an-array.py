#
# @lc app=leetcode id=2221 lang=python3
#
# [2221] Find Triangular Sum of an Array
#

# @lc code=start
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        prev = nums
        curr = [0] * n

        for k in range(n-1, 0, -1):
            for i in range(k):
                curr[i] = (prev[i] + prev[i+1]) % 10

            #print(curr[:k])
            prev = curr

        return curr[0]
            
        
# @lc code=end

