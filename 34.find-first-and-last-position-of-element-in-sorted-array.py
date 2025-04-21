#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
def find_first(nums, target):
    left = 0
    right = len(nums)
    index =  -1
    while left < right:
        mid = (left + right) //2
        if nums[mid] == target:
            index = mid
            
        if nums[mid] >= target:
            right = mid -1
        else:
            left = mid
            
    if index == len(nums):
        return -1
    #We will never actully cehck the very first element
    if 0 < len(nums) and nums[0] == target:
        return 0
    return index

def find_last(nums, target):
    left = 0
    right = len(nums)
    index = -1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            index = mid
        if nums[mid] > target:
            right = mid -1 
        else:
            left = mid + 1
    #We will never actually check if the last elemet is equal to target
    if index+1 < len(nums) and nums[index+1] == target:
        return index+1
    return index
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #bisect left and bisect right 
        first_idx = find_first(nums, target)
        last_idx = find_last(nums, target)
        #print(first_idx, nums[first_idx])
        return [first_idx, last_idx]
        
        
        
# @lc code=end

