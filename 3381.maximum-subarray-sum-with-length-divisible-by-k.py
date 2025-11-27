#
# @lc app=leetcode id=3381 lang=python3
#
# [3381] Maximum Subarray Sum With Length Divisible by K
#

# @lc code=start
MAX = (1 << 53) -1
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        """
        two pointer approach. 
        start pointer and end pointer of each subarray
        or is it a prefix sum thing?
        no wait it is the size of the subarry that needs to be divisible by K

        prefix sum ending at every possible index%k
        we dont actually have the say which array have the maximum, 
        so we can just keep track of everything mod k 
        """
        n = len(nums)
        min_sum =[MAX]*(k-1) + [0]
        prefix = 0
        result = -MAX

        
        for i, num in enumerate(nums):
            prefix += num
            index = i % k
            result = max(result, prefix - min_sum[index])
            min_sum[index] = min(prefix, min_sum[index])
        return result
        
            



        
# @lc code=end

