#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] *(n+1)
        for i in range(n+1):
            result[i] = result[i >> 1] + (i & 1)
        return result
    
class Solutionv1:
    def popCount(self, x: int) -> int:
        count = 0
        while x > 0:
            count += (x & 1)
            x = x >> 1
        return count 

    def countBits(self, n: int) -> List[int]:
        result = [0] *(n+1) 
        for i in range(n+1):
            result[i] = self.popCount(i)
        return result
            
        
# @lc code=end

