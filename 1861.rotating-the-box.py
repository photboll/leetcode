#
# @lc app=leetcode id=1861 lang=python3
#
# [1861] Rotating the Box
#

# @lc code=start
def active_gravity(grid: list[list[str]]) -> List[List[str]]:
    m = len(grid)
    n = len(grid[0])
    
    for c in range(n):
        prev_obstacle = m
        for r in range(m-1, -1, -1):
            if grid[r][c] == "#":
                #let stone fall to the position just above the previous obstacle
                grid[prev_obstacle-1][c] = "#"
                if prev_obstacle -1 != r:#Did the stone actually move?
                    grid[r][c] = "."
                # previous obstacle will be the current stone (else stones will pass through each other)
                prev_obstacle -= 1
            elif grid[r][c] == "*":
                #update obstacle points
                prev_obstacle = r
    
def rotate90(matrix):
    #rotating 90 is the same as transpose(reverse_rows(matrix))
    return [list(row) for row in zip(*matrix[::-1])]

    
            
            
class Solution:

    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:

        #print(boxGrid)
        boxGrid = rotate90(boxGrid)
        active_gravity(boxGrid)
        #print(boxGrid)
        return boxGrid

        
# @lc code=end

