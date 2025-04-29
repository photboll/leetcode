#
# @lc app=leetcode id=2352 lang=python3
#
# [2352] Equal Row and Column Pairs
#

# @lc code=start
from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_idxs = defaultdict(list)
        result = 0
        for r in range(n):
            row_idxs[tuple(grid[r])].append(r)
        
        #print(row_idxs)
        for c in range(n):
            col = tuple(grid[r][c] for r in range(n))
            #print(col)
            result += len(row_idxs[col])
            
        
        return result
        
# @lc code=end

