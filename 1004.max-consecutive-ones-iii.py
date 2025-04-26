#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        as long as a window have less then or equal nmber of 0s compared to k.
        if we exceed k 0s we need to mame the window smaller
        """
        n = len(nums)
        
        zeros_in_window = 0
        max_len = 0
        left = 0
        for right in range(n):
            if nums[right] == 0:
                zeros_in_window += 1
            
            while zeros_in_window > k:
                if nums[left] == 0:
                    zeros_in_window -= 1
                left += 1
                
            max_len = max(max_len, right - left+1)
            #print(nums[left:right+1], left, right,max_len)
        return max_len 
            
        
# @lc code=end

