# @lc app=leetcode id=2897 slug=apply-operations-on-array-to-maximize-sum-of-squares lang=python3
#
# [2897] Apply Operations on Array to Maximize Sum of Squares
# Difficulty: Hard
# Tags: Array, Hash Table, Greedy, Bit Manipulation
# URL: https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/
#
# @lc code=start
MOD = pow(10, 9) + 7

MAX_BITS = 30
class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        """
        the AND OR operation described wil preserve the number of set bits in the output
        
        since we can use the operation any number of times we can redistribute the number of set 
        bits across k numbers to maximize the sum of squares. 
        
        """
        
        count = [0] * MAX_BITS

        for x in nums:
            for b in range(MAX_BITS):
                if x >> b & 1:
                    count[b] += 1
        
        result = 0

        for _ in range(k):
            curr = 0

            for b in range(MAX_BITS):
                if count[b] > 0:
                    count[b] -= 1

                    curr |= 1 << b
            result = (result + curr * curr) % MOD

        return result 


        

# @lc code=end
