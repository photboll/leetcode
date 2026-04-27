#
# @lc app=leetcode id=1391 lang=python3
#
# [1391] Check if There is a Valid Path in a Grid
#

# @lc code=start

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        if m == 1 and n == 1:
            return True
                
        transitions = [
            [-1, 1, -1, 3],
            [0, -1, 2, -1],
            [3, 2, -1, -1],
            [1, -1, -1, 2],
            [-1, 0, 3, -1],
            [-1, -1, 1, 0]
        ]
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        start = [[1, 3], [0, 2], [2, 3], [1, 2], [0, 3], [0, 1]]               

        
        def validate(d):
            if d == -1: return False
            r, c = directions[d]

            while 0 <= r < m and 0 <= c < n:
                d = transitions[grid[r][c] - 1][d] 
                if d == -1: return False
                if r == 0 and c == 0: return False
                if r == m-1 and c == n-1: return True

                dr, dc = directions[d]
                r += dr
                c += dc
            return False
        
        opt1, opt2 = start[grid[0][0]-1]
        return validate(opt1) or validate(opt2)



                    
        
# @lc code=end

