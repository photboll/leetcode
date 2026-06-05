#
# @lc app=leetcode id=3751 lang=python3
#
# [3751] Total Waviness of Numbers in Range I
#

# @lc code=start
from collections import deque
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def waviness(num):
            result = 0
            num, prev = divmod(num, 10)
            num, curr = divmod(num, 10)

            while num > 0:
                num, next = divmod(num, 10)

                if ((prev > curr < next) or #Valley 
                    (prev < curr > next)): #peak
                    result += 1

                #print(num, prev, curr, next, result)
                
                prev, curr = curr, next
            
            return result
        
        total = 0
        for num in range(num1, num2+1):
            total += waviness(num)
            
        return total
        
# @lc code=end

