#
# @lc app=leetcode id=2780 lang=python3
#
# [2780] Minimum Index of a Valid Split
#

# @lc code=start
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        #More than half the elements of arr have a value of x.
        #it is the majority element in its part, a plurality is not enough 
        #this make the problem sligthly easier,
        #Since we only need to know the count of element x in each subarray to determine if it is dominant 
        #1. Determine the count of the dominant element in arr
        #2. Keep a count of how many xs are in on the left, and right side of the split point.
        #3. traverse the array for each possilbe split point and check if x is dominant in both subarrays
        
        count = 1
        x = nums[0]
        for num in nums[1:]:
            if x == num:
                 count+= 1
            else:
                count -=1
            if count < 0:
                x = num 
                count = 1
        #print(x, count)

        #count = totalCount of x - totalCount not x 
        #can we compute the actual number of x from this? 
        #We also know that len(nums) = totalCount of x + totalCount not x
        #so (count + len(nums) ) = 2* totalCount of x
        #rightCountX = (count + len(nums)) // 2 
        rightCountX = nums.count(x)
        leftCountX = 0
        #print(x, count, rightCountX, leftCountX)
        for i in range(len(nums) -1 ):
            if nums[i] == x :
                leftCountX += 1
                rightCountX -= 1
            if leftCountX * 2 > (i + 1) and rightCountX * 2 > (len(nums) - (i + 1)):
                return i
        
        return -1       
# @lc code=end

