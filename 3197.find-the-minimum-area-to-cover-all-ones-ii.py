#
# @lc app=leetcode id=3197 lang=python3
#
# [3197] Find the Minimum Area to Cover All Ones II
#

# @lc code=start
def print_grid(sub_grid):
    for row in sub_grid:
        print(row)

def print_splits(grid):
    print("Complete")
    print_grid(grid)
    print("Splits")
    for vsplit in range(1, len(grid)):
        print(vsplit)
        print_grid(grid[:vsplit])
        print("______")
        print_grid(grid[vsplit:])
    print("Horizontal")
    for hsplit in range(1, len(grid[0])):
        print(hsplit)
        print_grid([row[:hsplit] for row in grid])
        print("______")
        print_grid([row[hsplit:] for row in grid])

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        """
        non overlapping rectangles implies that we can subdivide the grid entirerly
        2 rectangles
        we either have to split the grid vertically or horizontally. m + n -2 number of split points  
        then we can split one of the two sub_grid once again.  for a total of 2*(m+n-2) split points to consider
        eah sub_grid can easily be calculated using formula from previous task  
        """
        def minimumRectangleCover(sub_grid)-> int: 
            m = len(sub_grid)
            n = len(sub_grid[0])

            topmost = m
            botmost = 0
            leftmost = n
            rightmost = 0

            for i in range(m):
                for j in range(n):
                    if sub_grid[i][j] == 1:
                        topmost = min(topmost, i)
                        botmost = max(botmost, i)
                        leftmost = min(leftmost, j)
                        rightmost = max(rightmost, j)
            
            #There are no 1s in the sub_grid 
            if topmost > botmost:
                return 0

            return (botmost - topmost + 1) * (rightmost - leftmost + 1)
        
        def vsplit_grid(grid, split_i):
            top = grid[:split_i]
            bot = grid[split_i:]
            return top, bot

        def hsplit_grid(grid, split_i):
            left = [row[:split_i] for row in grid]
            right = [row[split_i:] for row in grid]
            return left, right

        def recur_split(grid, num_splits=1) -> int:
            if not grid:
                return float("inf")
            if num_splits < 1:
                covered_area = minimumRectangleCover(grid)
                if covered_area == 0:
                    #all rectangles have to be non empty
                    return float("inf")
                else:
                    return covered_area
            
            res = float("inf")
            for vsplit in range(1, len(grid)):
                top, bot = vsplit_grid(grid, vsplit)
                #We can only split top or bottom (in this problem)
                split_top = recur_split(top, num_splits-1) + recur_split(bot, num_splits-2)
                split_bot = recur_split(top, num_splits-2) + recur_split(bot, num_splits-1)

                res = min(res, split_bot, split_top)
                
            
            for hsplit in range(1, len(grid[0])):
                left, right = hsplit_grid(grid, hsplit)
                split_left = recur_split(left, num_splits-1) + recur_split(right, num_splits-2)
                split_right = recur_split(left, num_splits-2) + recur_split(right, num_splits-1)
                res = min(res, split_left, split_right)
            
            return res
            
        
        return recur_split(grid, num_splits=2)
            
        
        
# @lc code=end

