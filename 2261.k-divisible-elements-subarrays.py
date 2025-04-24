#
# @lc app=leetcode id=2261 lang=python3
#
# [2261] K Divisible Elements Subarrays
#

# @lc code=start
class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        distinct_subarrays = set()
        window_div_p = 0
        left = 0
        n = len(nums)
        for right in range(n):
            window_div_p += (nums[right] % p == 0) 
            #Need to shrink the window if we excced k
            while window_div_p > k:
                is_divisble = (nums[left] % p == 0)
                window_div_p -= is_divisble
                distinct_subarrays.add(tuple(nums[left:right]))
                left += 1
            
            for i in range(left, right):
                distinct_subarrays.add(tuple(nums[i:right]))
            
            #print(distinct_subarrays)
        #print(left, right)
        for i in range(left, n):
            distinct_subarrays.add(tuple(nums[i:]))
        #print(distinct_subarrays)
        return len(distinct_subarrays)
            
        
        
        
# @lc code=end

