#
# @lc app=leetcode id=1590 lang=python3
#
# [1590] Make Sum Divisible by P
#

# @lc code=start
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        """
        prefix sum array and then twopointer 
        all numbers are positive in 
        
        """
        target = sum(nums) % p
        if target == 0:
            return 0

        cur_sum = 0
        #indices holds the last seen index which had a specific cur_sum % p
        #0:-1 is important in order to consider subarrays that start at the first position
        indices = {0:-1}
        min_len = len(nums)
        for i, num in enumerate(nums):
            cur_sum = (cur_sum + num) % p


            diff = (cur_sum - target + p ) % p
            #nums[indices[diff]:i+1] is a subarray with sum % p == target
            if diff in indices:
                min_len = min(min_len, i- indices[diff])

            indices[cur_sum] = i

        if min_len == len(nums): 
            return -1
        return min_len


        
# @lc code=end

