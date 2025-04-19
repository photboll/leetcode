#
# @lc app=leetcode id=2563 lang=python3
#
# [2563] Count the Number of Fair Pairs
#

# @lc code=start
def search_insert_position(nums, target):
    low = 0
    high = len(nums)
    while low< high:
        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid
    
    if low < len(nums) and nums[low] < target:
        return low +1 
    else:
        return low
    
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)):
            num = nums[i]
            #Count nums >=lower -num and nums <=upper - num
            idx_ge_lower = search_insert_position(nums, lower-num)
            if idx_ge_lower <= i:
                idx_ge_lower = i+1 
                

            idx_le_upper = search_insert_position(nums, upper-num +1)# +1 to get including upper boundary
            #print(i , num, nums[idx_ge_lower:idx_le_upper],idx_ge_lower, idx_le_upper)
            
            #Since nums is sorted as soon as the upper boundary falls below the lower boundary
            #There will be no more valid pairs     
            if idx_le_upper < idx_ge_lower:
                break
            count += idx_le_upper - idx_ge_lower
            
        return count
            
             
                
    
class SolutionV1:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        #Presumably the brute force solution is too slow since this is a medium problem 
        #But the constraints are relatively small, maybe it can work
        #We ran into TLE with the bruteForce
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if lower <= nums[i] + nums[j] <= upper:
                    count += 1
        
        return count
# @lc code=end

