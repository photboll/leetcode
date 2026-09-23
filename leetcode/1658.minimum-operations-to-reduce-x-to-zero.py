# @lc app=leetcode id=1658 slug=minimum-operations-to-reduce-x-to-zero lang=python3
#
# [1658] Minimum Operations to Reduce X to Zero
# Difficulty: Medium
# Tags: Array, Hash Table, Binary Search, Sliding Window, Prefix Sum
# URL: https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
#
# @lc code=start
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        """
        equivalent to finding the maximum(length) subarry that is equal to sum(nums) -x 

        """
        n = len(nums)
        s = sum(nums)
        window_sum = 0
        target_sum = s - x
        if target_sum < 0:
            return -1
        result = -1

        l = 0

        for r in range(n):
            window_sum += nums[r]

            while window_sum > target_sum:
                window_sum -= nums[l]
                l += 1
            
            if window_sum == target_sum and r - l + 1 > result:
                result = r - l+1
            
        return n - result if result > -1 else -1
            
            

            
            


            


        


        

# @lc code=end
