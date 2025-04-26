#
# @lc app=leetcode id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#

# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        Vary similar to longest sequence of ones with at most one zero in it 
        there should only be a difference when the array is filled with only ones 
        """
        n = len(nums)
        zeros_in_window = 0
        max_len = 0
        left = 0
        for right in range(n):
            if nums[right] == 0:
                zeros_in_window += 1
            
            while zeros_in_window > 1:
                if nums[left] == 0:
                    zeros_in_window -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1 - zeros_in_window)
        #if max_len is the same as the entire array, we are forced to delete a single 1
        return min(n-1, max_len)
        
        
# @lc code=end

