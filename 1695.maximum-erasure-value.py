#
# @lc app=leetcode id=1695 lang=python3
#
# [1695] Maximum Erasure Value
#

# @lc code=start
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """
        Sliding window
        Only positive integers: 
        if we can make the window larger without containing duplicates a larger window is always better
        Dont know why they have rephrased it as a score of deleting a value.
        We want to find the largest subarray sum that only contains unique elements
        """
        n = len(nums)
        res = 0 # it is unclear if an empty subarray is a valid deletion 
        window_sum = 0
        window = set()
        l = 0
        for r in range(n):
            
            #print(l, r, window)
            while l < r and nums[r] in window:
                window.remove(nums[l])
                window_sum -= nums[l]
                l += 1
            
            window_sum += nums[r]
            window.add(nums[r])

            res = max(res, window_sum)
        return res
            
            
            
             
        
# @lc code=end

