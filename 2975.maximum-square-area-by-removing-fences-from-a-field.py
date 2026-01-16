#
# @lc app=leetcode id=2975 lang=python3
#
# [2975] Maximum Square Area by Removing Fences From a Field
#

# @lc code=start
from heapq import heappush, heappop

MOD = pow(10, 9) + 7
class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        """  
        add 1 and m to hFences. difference between any two values can be a horizontal edge
        same for vFences
        
        since we can remove arbitrary number of fences, it does not matter how many fences are between 
        that is alot of edges to consider. m**2 + n**2 
        
        if we go through from largest to smallest, we can exit early 

        """
        def fences_to_edges(fences, size):
            points = sorted([1] + fences + [size])
            return {
                points[j] - points[i] 
                for i in range(len(points))
                for j in range(i+1, len(points))
            }
        
        hEdges = fences_to_edges(hFences, m)
        vEdges = fences_to_edges(vFences, n)

        side = max( vEdges & hEdges, default=0)
        if side:
            return (side * side) % MOD
        else:
            return -1


            
        

                



        
# @lc code=end

