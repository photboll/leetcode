#
# @lc app=leetcode id=869 lang=python3
#
# [869] Reordered Power of 2
#

# @lc code=start

from collections import Counter
import math
def count_digits(n : int) -> List[int]:
    freqs = [0] * 10
    if n == 0:
        freqs[0] += 1

    while n > 0:
        n, digit = divmod(n, 10)
        freqs[digit] += 1
    return freqs
MAX_BIT_LEN = 32   
P2DIGITS = set()
for i in range(MAX_BIT_LEN):
    P2DIGITS.add( tuple(count_digits(1 << i)))

    
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        """
        we cannot lose digits by reordering. so for any given number there is only a small number
        of possible target power of 2s. it can only be 3-4 
        0 <= n <= 10e9
        """
        freqs = tuple(count_digits(n))
        return freqs in P2DIGITS


        
        
# @lc code=end

