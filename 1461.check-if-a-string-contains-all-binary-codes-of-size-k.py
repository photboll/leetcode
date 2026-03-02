#
# @lc app=leetcode id=1461 lang=python3
#
# [1461] Check If a String Contains All Binary Codes of Size K
#

# @lc code=start
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()
        l = 0
        for r in range(k, len(s)):
            seen.add(s[l: r+1])
            l += 1
        return pow(2, k) == len(seen)
        
# @lc code=end

