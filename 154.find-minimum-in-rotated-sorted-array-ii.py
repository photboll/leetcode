#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        We still need to find the inflection point.
        but now we run into the problem of equality.
        we have a divergent scenario where all numbers are equal
        then we will never find an inflection point.
        What else do we know about the minimum
        we know that its left neighbor must be greater or equal to itself.
        equality only happens if all numbers are the same 
        
        """
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if (nums[l] == nums[mid] == nums[r]):
                l += 1
                r -= 1
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
                
        return nums[l]
            
        
# @lc code=end

