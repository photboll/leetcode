#
# @lc app=leetcode id=1878 lang=python3
#
# [1878] Get Biggest Three Rhombus Sums in a Grid
#

# @lc code=start
from heapq import heappop, heappush, heapreplace, heapify

class TopKPriorityQueue:
    def __init__(self, vals):
        #Vals is a list of the values which can not increase or decrease in size
        heapify(vals)
        self.pq = vals
        self.set = set(vals)
    
    def replace(self, val):
        if val > self.pq[0] and val not in self.set:
            old = heapreplace(self.pq, val)
            self.set.discard(old)
            self.set.add(val)

    def to_list(self):
        # Return sorted distinct values in descending order, filtering out placeholders
        res = sorted([x for x in self.pq if x != float("-inf")], reverse=True)
        return res


    
class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        """
        Since 0 size rhombuses are allowed, we will only ever have less than 3 answers if there are less than thre entries
        additionally since the limit is set to 3, there will only ever be 0 size rhombuses in this case. since size one requires a grid of 2 X 2 
        """
        

        m = len(grid)
        n = len(grid[0])
        max_size = min(m, n)
        pq = TopKPriorityQueue([float("-inf")] * 3)

        #diagonal prefix sums
        dr = [[0]*n for _ in range(m)]#Down right 
        dl = [[0]*n for _ in range(m)]#down left
        for r in range(m):
            for c in range(n):
                dr[r][c] = grid[r][c]
                dl[r][c] = grid[r][c]

                if r > 0 and c > 0:
                    dr[r][c] += dr[r-1][c-1]
                
                if r > 0 and c+1 < n:
                    dl[r][c] += dl[r-1][c+1]
                    
                
        #check all rhombus sizes
        for r in range(m):
            for c in range(n):
                pq.replace(grid[r][c])
                # k is the radius of the rhombus
                for k in range(1, max_size):
                    #if any vertice lies outside of the grid
                    #then it is invalid and we have already processed the largest rhombus with top at r, c
                    if r + 2*k >= m or c + k >= n or c - k < 0:
                        break
                    
                    curr = dr[r+k][c+k] - dr[r][c]#Top to right
                    curr += dl[r+2*k][c] - dl[r+k][c+k]# right to bot
                    curr += dr[r+2*k][c] - dr[r+k][c-k]# bot to left
                    curr += dl[r+k][c-k] - dl[r][c]#left to top 
                    
                    # Right and Left are included once. Bottom is included twice. Top is excluded.
                    # Correct by adding Top once and subtracting the duplicate Bottom.
                    curr += grid[r][c]#top
                    curr -= grid[r+2*k][c]#bot

                    #add it to the heap
                    pq.replace(curr)
        
        return pq.to_list()
                                      
            


            

        
# @lc code=end

