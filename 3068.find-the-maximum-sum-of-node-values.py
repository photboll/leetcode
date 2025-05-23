#
# @lc app=leetcode id=3068 lang=python3
#
# [3068] Find the Maximum Sum of Node Values
#

# @lc code=start
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        memo = [[-1] * 2 for _ in range(len(nums))]
        def maxSum(index, isEven):
            if index == len(nums):
                return 0 if isEven else -float("inf")
            
            if memo[index][isEven] != -1:
                return memo[index][isEven]
            
            #We can either xor a number with k or not do it 
            no_xor_done = nums[index] + maxSum(index+1, isEven)
            xor_done =(nums[index] ^ k) + maxSum(index+1, not isEven)
            

            memo[index][isEven] = max(xor_done, no_xor_done)
            return memo[index][isEven]
            
        
        return maxSum(0, 1)
            

        
        
        
        
# @lc code=end

