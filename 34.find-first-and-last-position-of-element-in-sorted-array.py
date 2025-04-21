#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
def find(nums, target, mode="first"):
    left, right = 0, len(nums) -1
    index = -1
    while left <= right :
        mid = (left + right) // 2
        
        if nums[mid] == target:
            index = mid
            if mode== "first":
                right = mid-1
            elif mode == "last":
                left = mid+1
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return index

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [find(nums, target, 'first'), find(nums, target, 'last')]


def find_first(nums, target):
    left = 0
    right = len(nums) -1
    index =  -1
    while left <= right:
        mid = (left + right) //2
            
        if nums[mid] >= target:
            right = mid -1
        else:
            left = mid + 1

        if nums[mid] == target:
            index = mid
            
    return index

def find_last(nums, target):
    left = 0
    right = len(nums)-1
    index = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid -1 
        else:
            left = mid + 1

        if nums[mid] == target:
            index = mid
    #We will never actually check if the last elemet is equal to target
    if index+1 < len(nums) and nums[index+1] == target:
        return index+1
    return index
class SolutionV1:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #bisect left and bisect right 
        first_idx = find_first(nums, target)
        last_idx = find_last(nums, target)
        #print(first_idx, nums[first_idx])
        return [first_idx, last_idx]
        
        
        
# @lc code=end

