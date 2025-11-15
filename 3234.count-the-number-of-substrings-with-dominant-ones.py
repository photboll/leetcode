#
# @lc app=leetcode id=3234 lang=python3
#
# [3234] Count the Number of Substrings With Dominant Ones
#

# @lc code=start
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        prev = [-1] *(n+1)
        for i in range(n):
            if i == 0 or s[i-1] == "0":
                prev[i+1] = i
            else:
                prev[i+1] = prev[i]

        result = 0
        for r in range(1, n+1):
            count0 = 1 if s[r-1] == "0" else 0
            j = r

            while j > 0 and count0 * count0 <= n:
                count1 = (r-prev[j]) - count0
                #print(r, j, count0, count1, prev)
                if count0 * count0 <= count1:
                    result += min(j - prev[j], count1 - count0 * count0 + 1)
                j = prev[j]
                count0 += 1
            
        
        return result
                
        
# @lc code=end

