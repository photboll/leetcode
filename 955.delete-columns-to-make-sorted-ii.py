#
# @lc app=leetcode id=955 lang=python3
#
# [955] Delete Columns to Make Sorted II
#

# @lc code=start
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cuts = [False] * (len(strs) - 1)

        res = 0
        for col in zip(*strs):
            if all(cuts[i] or col[i] <= col[i+1] for i in range(len(col) - 1)):
                for i in range(len(col) -1):
                    if col[i] < col[i+1]:
                        cuts[i] = True
            else:
                res += 1
        return res 

                

        
# @lc code=end

