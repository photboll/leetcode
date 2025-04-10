#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        sym2i = {"I": 1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000,
                 "IV": 4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
        tot = 0
        i = 0
        
        while i < len(s) -1:
            #First try to match it as a subtraction
            if s[i:i+2] in sym2i:
                tot += sym2i[s[i:i+2]]
                i+= 2
            else:
                tot += sym2i[s[i]]
                i += 1
        if i < len(s):
            tot += sym2i[s[i]]
        return tot
             
        
# @lc code=end

