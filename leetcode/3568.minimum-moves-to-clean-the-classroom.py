# @lc app=leetcode id=3568 slug=minimum-moves-to-clean-the-classroom lang=python3
#
# [3568] Minimum Moves to Clean the Classroom
# Difficulty: Medium
# Tags: Array, Hash Table, Bit Manipulation, Breadth-First Search, Matrix
# URL: https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/
#
# @lc code=start
from collections import deque, defaultdict

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])
        sx = sy = -1
        #dict to map (position, to litters position in the mask)
        litter = {}#

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == "S":
                    sx = i
                    sy = j
                elif classroom[i][j] == "L":
                    litter[(i, j)] = len(litter)
            
        full_mask = (1 << len(litter)) - 1
        #print(litter, bin(full_mask))
                    
            
        q = deque()
        #(number_of_steps, starting_x, starting_y, current_mask, current_energy)
        q.append((0, sx, sy, energy, 0))
        best_energy = {(sx, sy, 0):energy}


        while q:
            steps, cx, cy, cur_e, mask= q.popleft()
            if (cx, cy) in litter:#set the mask
                mask |= (1 << litter[(cx, cy)])
            
            if mask == full_mask:
                return steps
            
            if classroom[cx][cy] == "R":
                cur_e = energy
            
            key = (cx, cy, mask)
            if cur_e < best_energy.get(key, -1):
                # A better state have already been explored
                continue  

            best_energy[key] = cur_e
            if cur_e <= 0:#Out of energy 
                continue
            
            for dx, dy in DIRECTIONS:
                nx = cx + dx
                ny = cy + dy
                if not (0 <= nx < m and 0 <= ny < n) or classroom[nx][ny] == "X":
                    #out of bounds
                    continue

                new_e = cur_e -1
                nkey = (nx, ny, mask)
                if new_e > best_energy.get(nkey, -1):
                    best_energy[nkey] = new_e
                    q.append((steps +1, nx, ny, new_e, mask))
        
        
        return -1

                
                
                

                


        

# @lc code=end
