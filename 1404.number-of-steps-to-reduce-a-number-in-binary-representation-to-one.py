#
# @lc app=leetcode id=1404 lang=python3
#
# [1404] Number of Steps to Reduce a Number in Binary Representation to One
#

# @lc code=start
class Solution:
    def numSteps(self, s: str) -> int:
        """  
        Dividing by two is the same as shifting left 
        +1 when the rightmost bit is one will create a carry 
        """
        n = len(s)
        carry = 0
        count = 0
        for i in range(n-1, 0, -1):
            bit = int(s[i]) + carry
            if bit == 1:
                count+= 2  
                carry = 1
            else:
                count += 1
        return count + carry

        
# @lc code=end

