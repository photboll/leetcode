#
# @lc app=leetcode id=2894 lang=python3
#
# [2894] Divisible and Non-divisible Sums Difference
#

# @lc code=start
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        """num1 + num2 = sum(range(1, n+1))
            num1 - num2 = ?
            num2 = tot_sum // m
        """
        tot_sum = n *(n+1) // 2
        k = n // m
        
        return tot_sum - k *(k+1) * m
        
# @lc code=end

