#
# @lc app=leetcode id=1464 lang=python3
#
# [1464] Maximum Product of Two Elements in an Array
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx1 = mx2 = 0
        for num in nums:
            if num > mx1:
                mx2 = mx1
                mx1 = num
            elif num > mx2:
                mx2 = num

        return (mx1-1) *(mx2 -1)
        
# @lc code=end

