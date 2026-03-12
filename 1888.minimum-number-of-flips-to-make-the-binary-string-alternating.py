#
# @lc app=leetcode id=1888 lang=python3
#
# [1888] Minimum Number of Flips to Make the Binary String Alternating
#

# @lc code=start
class Solution:
    def minFlips(self, s: str) -> int:
        """ 
        How do i best utilize op1 ? the cyclic shift
        is it ever worth doing more than 2 shifts?
        yes it is if the string is 000110000 then shifting it to be 10000001
        the important property of the shift is that we can push a bit 
        from being in an odd position to an even position

        do I have to try all possible number of shifts?
        
        """
        n = len(s)
        cnts0 = [0, 0]
        cnts1 = [0, 0]
        s = list(map(int, s))
        res = float("inf")

        for i, digit in enumerate(s):
            cnts0[(i&1)^digit] += 1
        
        if not n % 2:
            #cycling does not help when s's length is even
            return min(cnts0)
        
        for i, digit in enumerate(s):
            cnts0[i&1^digit] -= 1
            cnts1[~i&1^digit] += 1
        
            res = min(res, 
                      cnts0[0] + cnts1[0],
                      cnts0[1] + cnts1[1])
        return res


        
# @lc code=end

