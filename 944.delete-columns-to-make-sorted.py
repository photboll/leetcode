#
# @lc app=leetcode id=944 lang=python3
#
# [944] Delete Columns to Make Sorted
#

# @lc code=start
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)

        res = 0
        for c in range(len(strs[0])):
            for r in range(1, n):
                if strs[r][c] < strs[r-1][c]:
                    res += 1
                    break

        return res
        
# @lc code=end

