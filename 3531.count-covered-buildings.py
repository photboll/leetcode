#
# @lc app=leetcode id=3531 lang=python3
#
# [3531] Count Covered Buildings
#

# @lc code=start
from collections import defaultdict
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        rows = defaultdict(list)
        cols = defaultdict(list)

        for r, c in buildings:
            rows[c].append(r)
            cols[r].append(c)
        
        row_min = {y: min(xs) for y, xs in rows.items()}
        row_max = {y: max(xs) for y, xs in rows.items()}
        col_min = {x: min(ys) for x, ys in cols.items()}
        col_max = {x: max(ys) for x, ys in cols.items()}

        
        covered = 0

        for x, y in buildings:
            if not (row_min[y] < x < row_max[y]):
                continue
            if not (col_min[x] < y < col_max[x]):
                continue
            
            covered += 1
        
        return covered


        
# @lc code=end

