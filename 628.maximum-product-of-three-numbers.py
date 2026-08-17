#
# @lc app=leetcode id=628 lang=python3
#
# [628] Maximum Product of Three Numbers
#

# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        #two negative and one positive 
        #or all positive
        mx1 = mx2 = mx2 = -1001
        mn1 = mn2 = 1001

        for num in nums:
            if num > mx1:
                mx3 = mx2
                mx2 = mx1
                mx1 = num
            elif num > mx2:
                mx3 = mx2
                mx2 = num
            elif num > mx3:
                mx3 = num

            if num < mn1:
                mn2 = mn1
                mn1 = num
            elif num < mn2:
                mn2 = num
    
        return max(mx1 * mx2 * mx3, mn1*mn2*mx1)

        
# @lc code=end

