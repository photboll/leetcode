#
# @lc app=leetcode id=761 lang=python3
#
# [761] Special Binary String
#

# @lc code=start
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if s == "":
            return ""
        
        n = len(s)
        res = []
        count = 0
        i =  0
        for j in range(n):
            if s[j] == "1":
                count += 1
            else:
                count -= 1
                
            #then s[j:i] is special
            if count == 0:
                res.append("1" + self.makeLargestSpecial(s[i+1:j]) + "0")
                i = j+1

        res.sort(reverse=True)
        return "".join(res)
            
        
# @lc code=end

