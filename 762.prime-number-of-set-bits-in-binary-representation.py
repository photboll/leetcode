#
# @lc app=leetcode id=762 lang=python3
#
# [762] Prime Number of Set Bits in Binary Representation
#

# @lc code=start
PRIMES = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 28])
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        """  
        max value is 10**6 so we will always have less than 32 bits 
        only need to check a small number of possible values 
        """
        res = 0
        for num in range(left, right+1):
            if num.bit_count() in PRIMES:
                res += 1
        return res

        
# @lc code=end

