#
# @lc app=leetcode id=1689 lang=python3
#
# [1689] Partitioning Into Minimum Number Of Deci-Binary Numbers
#

# @lc code=start
class Solution:
    def minPartitions(self, n: str) -> int:
        res = 0
        for char in n:
            res = max(res, int(char))
        return res
        
# @lc code=end

