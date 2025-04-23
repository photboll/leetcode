#
# @lc app=leetcode id=1248 lang=python3
#
# [1248] Count Number of Nice Subarrays
#

# @lc code=start
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
        Sliding window approach, 
        what matters is the number of odd numbers in the window
        """
        left = 0
        odd_numbers_wihtin =  0
        n = len(nums)
        count = 0
        for right in range(n):
            #Add the number at nums[right] to the window
            if nums[right] % 2 == 1:
                odd_numbers_wihtin += 1
            
               
            #Did we exceed the limit, then shrink the current window 
            while odd_numbers_wihtin > k and left < right:
                if nums[left] % 2 == 1:
                    odd_numbers_wihtin -= 1
                else:
                    left += 1
                    
            if odd_numbers_wihtin == k:
                count += right - left

        return count 
            
            
                
            
            
            
        
# @lc code=end

