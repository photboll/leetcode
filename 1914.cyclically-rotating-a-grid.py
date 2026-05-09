#
# @lc app=leetcode id=1914 lang=python3
#
# [1914] Cyclically Rotating a Grid
#

# @lc code=start
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def rotate_arr(arr, k):
    rot = k % len(arr)
    return arr[rot:] + arr[:rot]

    
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        #layer of array to 1d array
        #rotate array k counter clockwise
        #map buffer bck to grid
        #repeat for next layer 

        #each layer starts at (i, i)  i must be less than min(m, n) // 2 + 1
        #how many entreis do we have in each layer?
        # first layer 2 * (m-1) + 2 * (n-1),. m and n should be modified for each layer 
        # what does it even mean to rotate a 1d slice counter clockwise. if m or n is odd then a layer will be 1d

        layers = min(m, n) // 2

        for layer in range(layers):
            vals = []

            top = layer
            left = layer
            bottom = m - layer - 1
            right = n - layer - 1

            for c in range(left, right+1):
                # top row
                vals.append(grid[top][c])
            
            for r in range(top+1, bottom):
                #right column
                vals.append(grid[r][right])
            
            for c in range(right, left-1, -1):
                #bottom row 
                vals.append(grid[bottom][c])
            
            for r in range(bottom -1, top, -1):
                #left column
                vals.append(grid[r][left])
            
            vals = rotate_arr(vals, k)
            idx = 0

            # write top row
            for c in range(left, right + 1):
                grid[top][c] = vals[idx]
                idx += 1

            # write right column
            for r in range(top + 1, bottom):
                grid[r][right] = vals[idx]
                idx += 1

            # write bottom row
            for c in range(right, left - 1, -1):
                grid[bottom][c] = vals[idx]
                idx += 1

            # write left column
            for r in range(bottom - 1, top, -1):
                grid[r][left] = vals[idx]
                idx += 1

        return grid





        
        
        
# @lc code=end

