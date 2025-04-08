#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Need to find the inflection point
        low = 0
        high = len(nums) -1
        while low < high:
            mid = (low+high) // 2
            if nums[mid] > nums[high]:
                low = mid+1
            else:
                high = mid
        
        return nums[low]
        
        
        
# @lc code=end

