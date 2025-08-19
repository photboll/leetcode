#
# @lc app=leetcode id=2348 lang=python3
#
# [2348] Number of Zero-Filled Subarrays
#

# @lc code=start
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        """
        Sliding window 
        """
        n = len(nums)
        total = 0
        l = -1
        for r in range(n):
            if nums[r] != 0:
                #k is the number of 0s in a row 
                k = r - l -1
                
                total += k *(k+1) // 2
                #print(l, r, k, total)
                l = r
        
        k = r -l
        if k > 0:
            total += k *(k+1) // 2
        
        #print(total)
        return total
                
        
# @lc code=end

