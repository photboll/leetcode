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
            for cuts_in_first in range(num_splits):
                cuts_in_second = (num_splits -1) - cuts_in_first

                for vsplit in range(1, len(grid)):
                    top, bot = vsplit_grid(grid, vsplit)
                    area = recur_split(top, cuts_in_first) + recur_split(bot, cuts_in_second)

                    res = min(res, area)
                    
                
                for hsplit in range(1, len(grid[0])):
                    left, right = hsplit_grid(grid, hsplit)
                    area = recur_split(left, cuts_in_first) + recur_split(right, cuts_in_second)
                    res = min(res, area)
            
            return res
            
        
        return recur_split(grid, num_splits=2)


import numpy as np
from typing import List, Dict, Tuple

class SolutionNP:
    def minimumSum(self, grid: List[List[int]]) -> int:
        """
        Calculates the minimum sum of areas of 3 non-overlapping rectangles
        that cover all the '1's in the grid.

        This implementation uses a general-purpose, memoized recursion that
        can be extended to solve for N rectangles by changing the initial
        number of cuts.
        
        For 3 rectangles, we need 2 cuts.
        """
        # Convert the input grid to a NumPy array for efficient view-based slicing.
        self.grid = np.array(grid, dtype=np.int8)
        
        # Memoization cache to store results of subproblems.
        # Key: (r, c, h, w, k) -> top-left corner, dimensions, and cuts remaining.
        # Value: The minimum area sum for that subproblem.
        self.memo: Dict[Tuple[int, int, int, int, int], int] = {}

        h, w = self.grid.shape
        
        # To get 3 rectangles, we need to make 2 cuts.
        num_cuts = 2
        
        return self._solve(0, 0, h, w, num_cuts)

    def _get_bounding_box_area(self, r: int, c: int, h: int, w: int) -> int:
        """
        Calculates the area of the minimal bounding box for 1s within a
        sub-grid defined by its coordinates and dimensions.
        This is the base case for the recursion (when k=0 cuts remain).
        """
        # Create a view of the sub-grid without copying data.
        sub_grid = self.grid[r:r+h, c:c+w]
        
        # Find the coordinates of all '1's within this view.
        rows, cols = np.where(sub_grid == 1)

        # If there are no '1's, this partition is invalid. Return infinity
        # to ensure it's never chosen as a minimum.
        if len(rows) == 0:
            return float('inf')

        # Calculate the area of the bounding box.
        height = rows.max() - rows.min() + 1
        width = cols.max() - cols.min() + 1
        
        return height * width

    def _solve(self, r: int, c: int, h: int, w: int, k: int) -> int:
        if k == 0:
            return self._get_bounding_box_area(r, c, h, w)
        
        memo_key = (r, c, h, w, k)
        if memo_key in self.memo:
            return self.memo[memo_key]

        min_total_area = float('inf')

        # Distribute the remaining k-1 cuts after this first cut.
        # cuts_in_first can range from 0 to k-1.
        for cuts_in_first in range(k):
            cuts_in_second = (k - 1) - cuts_in_first

            # Try horizontal cuts
            for i in range(1, h):
                area = (self._solve(r, c, i, w, cuts_in_first) + 
                        self._solve(r + i, c, h - i, w, cuts_in_second))
                min_total_area = min(min_total_area, area)

            # Try vertical cuts
            for j in range(1, w):
                area = (self._solve(r, c, h, j, cuts_in_first) + 
                        self._solve(r, c + j, h, w - j, cuts_in_second))
                min_total_area = min(min_total_area, area)
        
        self.memo[memo_key] = min_total_area
        return min_total_area
            
        
        
# @lc code=end

