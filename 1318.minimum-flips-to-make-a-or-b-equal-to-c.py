#
# @lc app=leetcode id=1318 lang=python3
#
# [1318] Minimum Flips to Make a OR b Equal to c
#

# @lc code=start
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        """
        for a given bitposition, a | b will either be equal to the target c 
        in which case no flip is necessary.
        if (a | b)[i] != c[i] then 
        at bitposition i:
        c[i] = 0 => Need to flip any set bits at a[i] or b[i] to 0
        
        """
        aorb = a | b 
        num_flips = 0
        i = 0
        while aorb > 0 or c > 0:
            if (aorb & 1) != (c & 1):
                if (c & 1):#set that bit in a XOR b
                    num_flips += 1
                else:#cs bit is zero and a or b's is 1
                    num_flips += (a & 1)#Flip the a bit if it is 1
                    num_flips += (b & 1)#Flip the b bit if it is 1
                   
            a >>= 1
            b >>= 1
            aorb >>= 1
            c >>= 1
            
        return num_flips 
        
# @lc code=end

