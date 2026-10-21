# @lc app=leetcode id=3863 slug=minimum-operations-to-sort-a-string lang=python3
#
# [3863] Minimum Operations to Sort a String
# Difficulty: Medium
# Tags: String
# URL: https://leetcode.com/problems/minimum-operations-to-sort-a-string/
#
# @lc code=start
class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        if all(s[i] <= s[i+1] for i in range(n-1)):
            return 0
        
        if n == 2:
            return -1
        
        mn, mx = min(s), max(s)
        if s[0] == mn or s[-1] == mx:
            return 1
        
        if mn in s[:-1] or mx in s[1:]:
            return 2
        
        return 3
        

# @lc code=end
