#
# @lc app=leetcode id=3461 lang=python3
#
# [3461] Check If Digits Are Equal in String After Operations I
#

# @lc code=start
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        a = [int(c) for c in s]
        for i in range(len(a) -1, 1, -1):
            for j in range(i):
                a[j] = (a[j] + a[j+1]) % 10
        return a[0] == a[1]
        


        
# @lc code=end

