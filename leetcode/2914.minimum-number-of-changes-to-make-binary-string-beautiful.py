# @lc app=leetcode id=2914 slug=minimum-number-of-changes-to-make-binary-string-beautiful lang=python3
#
# [2914] Minimum Number of Changes to Make Binary String Beautiful
# Difficulty: Medium
# Tags: String
# URL: https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/
#
# @lc code=start
class Solution:
    def minChanges(self, s: str) -> int:
        """
        there is no incentive to make the partitions as large as possible
        
        """
        
        res = 0

        for i in range(0, len(s), 2):
            if s[i] != s[i+1]:
                res += 1
        
        return res
        

# @lc code=end
