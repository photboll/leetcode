# @lc app=leetcode id=462 slug=minimum-moves-to-equal-array-elements-ii lang=python3
#
# [462] Minimum Moves to Equal Array Elements II
# Difficulty: Medium
# Tags: Array, Math, Sorting
# URL: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
#
# @lc code=start

import random

def quickselect(nums, k):
    l, r = 0, len(nums) -1

    while l <= r:
        pivot = nums[random.randint(l, r)]
        i, j = l, r

        while i <= j:
            while nums[i] < pivot:
                i += 1
            while nums[j] > pivot:
                j -= 1

            #swap
            if i <= j:
                nums[i], nums[j] = nums[j] , nums[i]
                i += 1
                j -= 1
        
        if k <= j:
            r = j
        elif k >= i:
            l = i
        else:
            return nums[k]
            
        
def median(nums):
    n = len(nums)
    if n% 2:
        return quickselect(nums, n//2)
    
    a = quickselect(nums, n//2 - 1)
    b = quickselect(nums, n//2)

    return (a + b) /2

class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        #can it be off by one dpending on rounding. yes it will be off 
        #we need median not mean
        #i think we can just truncate it to an int since any target between the two middle elements should have the same result
        target = int(median(nums))

        res = 0
        for num in nums:
            res += abs(target - num)
        
        return res

        

# @lc code=end
