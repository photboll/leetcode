#
# @lc app=leetcode id=788 lang=python3
#
# [788] Rotated Digits
#

# @lc code=start
class Solution:
    def rotatedDigits(self, n: int) -> int:
        """
        In order for a number to be good
            1. at least one digit must map to a different char
            2. no digit can be mapped to an invalid digit 

        1 implies n must contain 2, 5, 6, 9
        2. implies n can not contain 3, 4, 7
        """

        def is_good(n: int):
            maps_to_different = False
            while n > 0:
                n, rem = divmod(n, 10)
                if rem in (2, 5, 6, 9):
                    maps_to_different = True
                elif rem in (3, 4, 7):
                    return False
            return maps_to_different
        
        res = 0
        for num in range(1, n+1):
            if is_good(num):
                res += 1
        return res 
        
        
# @lc code=end

