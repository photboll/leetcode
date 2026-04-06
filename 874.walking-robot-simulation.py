#
# @lc app=leetcode id=874 lang=python3
#
# [874] Walking Robot Simulation
#

# @lc code=start
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]# N, E, S ,W
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = set([(o[0], o[1]) for o in obstacles])
        x, y = 0, 0
        result = 0
        dir = 0

        for command in commands:
            if command == -2:#turn left
                dir = (dir -1 + 4) % 4
                continue
            elif command == -1:#turn right
                dir = (dir +1 + 4) % 4
                continue
            
            dx, dy = DIRECTIONS[dir]
            for _ in range(command):
                nx = x + dx
                ny = y + dy
                if (nx, ny) in obs:
                    break 
                x = nx
                y = ny
                result = max(result, x**2 + y**2)
        return result
        



        
# @lc code=end

