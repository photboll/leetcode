#
# @lc app=leetcode id=3713 lang=python3
#
# [3713] Longest Balanced Substring I
#

# @lc code=start
class Solution:
    def longestBalanced(self, s: str) -> int:
        count = 1
        n = len(s)
        for l in range(n):
            freq=[0]*26
            unique=0
            maxF = 0
            count_max = 0
            for r in range(l, n):
                freq[ord(s[r])-97] +=1
                f = freq[ord(s[r])-97]
                unique += f == 1
                if f > maxF:
                    maxF=f
                    count_max =1
                elif f == maxF:
                    count_max += 1
                if unique == count_max:
                    count = max(count, r-l+1)
        return count
                
        
# @lc code=end

