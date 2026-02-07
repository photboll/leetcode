#
# @lc app=leetcode id=1653 lang=python3
#
# [1653] Minimum Deletions to Make String Balanced
#

# @lc code=start
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        suffix_a = s.count("a")
        prefix_b = 0
        res = n

        for i in range(n):
            if s[i] == "a":
                suffix_a -= 1
            res = min(res, suffix_a + prefix_b)
            if s[i] == "b":
                prefix_b += 1

            
        return res



        
# @lc code=end

