#
# @lc app=leetcode id=3661 lang=python3
#
# [3661] Maximum Walls Destroyed by Robots
#

# @lc code=start
from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        ws = sorted(walls)

        order = sorted(range(n), key=lambda i: robots[i])
        pos  = [robots[i]   for i in order]
        dist = [distance[i] for i in order]

        def count(lb: int, ub: int) -> int:
            if lb > ub: return 0
            return bisect_right(ws, ub) - bisect_left(ws, lb)

        def left_walls(i: int) -> int:
            lb = max(pos[i] - dist[i], pos[i-1] + 1) if i > 0 else pos[i] - dist[i]
            return count(lb, pos[i])

        def right_walls(i: int) -> int:
            ub = min(pos[i] + dist[i], pos[i+1] - 1) if i < n-1 else pos[i] + dist[i]
            return count(pos[i], ub)  # FIX: was pos[i]+1

        def overlap(i: int) -> int:
            # Double-counted only when robot i-1 shoots RIGHT and robot i shoots LEFT
            lb = max(pos[i]   - dist[i],   pos[i-1] + 1)
            ub = min(pos[i-1] + dist[i-1], pos[i]   - 1)
            return count(lb, ub)

        dpL = left_walls(0)
        dpR = right_walls(0)

        for i in range(1, n):
            ol = overlap(i)
            lw = left_walls(i)
            rw = right_walls(i)

            new_dpL = max(dpL + lw, dpR + lw - ol)  # prev=R needs overlap subtracted
            new_dpR = max(dpL, dpR) + rw             # prev direction never overlaps with R shot

            dpL, dpR = new_dpL, new_dpR

        return max(dpL, dpR)
        


        
# @lc code=end

