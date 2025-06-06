#
# @lc app=leetcode id=2434 lang=python3
#
# [2434] Using a Robot to Print the Lexicographically Smallest String
#

# @lc code=start
from collections import Counter
class Solution:
    def robotWithString(self, s: str) -> str:
        """
        can we do it greedily, perfrom the operatino with the smallest char at each step?
        How would we deal with ties? 
        "bcdefab"
        here we have a tie, 
        if we start with the first b we get, "bbacdef"
        if we start with the secon b we get, "babcdef" which is smaller.
        
        if we have a tie is it enough, to look at the next chars?
        No wait i have misunderstod the task. i completely ignored the robot.
        teh operations act on different strigs.
        the robot seems to be acting like a stack.
        first opeeration is to move the first char of s to the stack
        second operation is to move the last char of t to the result
        """
        counts = Counter(s)
        res = []
        stack = []
        min_char = "a"
        
        for c in s:
            stack.append(c)
            counts[c] -= 1
            
            while min_char != "z" and counts[min_char] == 0:
                min_char = chr(ord(min_char) + 1)
            
            while stack and stack[-1] <= min_char:
                res.append(stack.pop())
                
        return "".join(res)

            
        
    
                
                
# @lc code=end

