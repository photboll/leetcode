#
# @lc app=leetcode id=1317 lang=python3
#
# [1317] Convert Integer to the Sum of Two No-Zero Integers
#

# @lc code=start
class Solution:
    def getNoZeroIntegers(self, n:int):
        n1, n2 = 0, 0
        pos = 1
        while n > 0:
            num = n % 10
            if num == 0:
                n1 += 1 *pos
                n2 += 9* pos
                n -= 10
            elif num == 1 and n>= 10:
                n1 += 2 *pos
                n2 += 9 *pos
                n -= 10
            else:
                n1 += (num-1)*pos
                n2 += 1 * pos
            pos *= 10
            n //= 10
            
        return [n1, n2]
class SolutionV1:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def contains_zero(num):
            for digit in str(num):
                if digit == "0":
                    return True
            return False

        for i in range(1, n //2+1):
            if not contains_zero(i) and not contains_zero(n-i):
                return [i, n-i]
        
            
        
# @lc code=end

