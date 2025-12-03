#
# @lc app=leetcode id=3625 lang=python3
#
# [3625] Count Number of Trapezoids II
#

# @lc code=start
from collections import defaultdict, Counter
from math import gcd
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        """
        similarily to the first version of this problem, we can first find 
        all line segments that are parallel and then compute all possible choices of pairwise parallel lines

        we need to compute the slope of every single possible line that can be made
        any two arbitrariy points 

        we also need to ensure that two lines in the same bucket does not coincide. since then 
        then it wont produce a quadrilateral
        """
        by_slope = defaultdict(Counter)
        by_vector = defaultdict(Counter)

        def calc_slope(p1, p2):
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]

            #Convention, fix a direction of the slop(right most in this)
            if dx < 0 or (dx == 0 and dy < 0):
                dx = -dx
                dy = -dy

            denom = gcd(dx, dy)
            ux = dx // denom
            uy = dy // denom

            line_id = ux * p1[1] - uy * p1[0]
            by_slope[(ux, uy)][line_id] += 1
            by_vector[(dx, dy)][line_id] += 1

        n = len(points)
        for i in range(n):
            p1 = points[i]
            for j in range(i+1, n):
                p2 = points[j]
                calc_slope(p1, p2)
        
        def count_pairs(mp):
            ans = 0
            for inner_map in mp.values():
                counts = inner_map.values()
                s = sum(counts)
                sum_sq = sum(c * c for c in counts )
                ans += (s * s - sum_sq) // 2
            return ans
        
        #each parallelogram will be double counted in the quadrilaterals
        #if we have A || B and C || D then the A B C D quadrilateral and the C D A B one will be counted 
        num_quadrilaterals = count_pairs(by_slope)
        num_parallelogram = count_pairs(by_vector) // 2

        return num_quadrilaterals - num_parallelogram
                

        
        
        
        
# @lc code=end

