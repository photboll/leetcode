#
# @lc app=leetcode id=2094 lang=python3
#
# [2094] Finding 3-Digit Even Numbers
#

# @lc code=start
from collections import Counter
class Solution:
    def findEvenNumbers(self, digits:List[int]) -> List[int]:
        freqs = Counter(digits)
        def can_make(num ):
            num_freqs = Counter([int(d) for d in str(num)])
            for key in num_freqs:
                if num_freqs[key] > freqs[key]:
                    return False
            return True
        
        result = []
        for num in range(100, 1000, 2):
            if can_make(num):
                result.append(num)
        return result
            
from itertools import permutations
def digits_to_int(digits):
    x = 0
    for digit in digits:
        x = 10 * x + digit
    return x
class SolutionBF:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        AT_LEAST = 100
        result = set()
        for perm in permutations(digits, 3):
            #print(perm)
            num = digits_to_int(perm)
            #print(num)
            if num >= AT_LEAST and num % 2 == 0:
                result.add(num)
        return sorted(list(result))

        
# @lc code=end

