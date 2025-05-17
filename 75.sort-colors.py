#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Count sort, we simply count the occurences of all colors and then fill it in inthe correct order
        but this will require two-passes, one to count, and one to move
        we can pass through it from both ends. since we only have three possible values we now that any two needs
        to be sent to the back of the array and any 0 to the front, we can simply count the number of ones we see and
        
        """
        counts = Counter(nums)# One pass 
        
        i = 0
        for k in range(3):
            for _ in range(counts[k]):
                nums[i] = k
                i += 1
        
            
        
        
# @lc code=end

