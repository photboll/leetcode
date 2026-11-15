# @lc app=leetcode id=1524 slug=number-of-sub-arrays-with-odd-sum lang=python3
#
# [1524] Number of Sub-arrays With Odd Sum
# Difficulty: Medium
# Tags: Array, Math, Dynamic Programming, Prefix Sum
# URL: https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/
#
# @lc code=start
MOD = pow(10, 9) + 7
class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        result = 0
        n =len(arr)
        sm = 0
        even_sums = 0
        odd_sums = 0

        for r in range(n):
            sm  = (sm + arr[r]) % 2
            # odd + odd = even
            # odd + even = odd
            # even + odd = odd
            #even + even = even

            if sm == 1:
                result = (result + sm + even_sums) % MOD
            elif sm == 0:
                result = (result + sm + odd_sums) % MOD

            
            if sm % 2 == 0:
                even_sums += 1
            else:
                odd_sums += 1
        
        return result
            
        

# @lc code=end
