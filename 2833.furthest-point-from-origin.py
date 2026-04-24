#
# @lc app=leetcode id=2833 lang=python3
#
# [2833] Furthest Point From Origin
#

# @lc code=start
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        """
        two scenarios eithe rmove left on all_ or right on all r
        """
        result = 0
        all_l = 0
        all_r = 0

        for char in moves:
            if char == "R":
                all_l += 1
                all_r += 1
            elif char == "L":
                all_l -= 1
                all_r -= 1
            else:
                all_l -= 1
                all_r += 1
            #print(all_l, all_r)
            
        return max(abs(all_l),
                    abs(all_r))
        
        
# @lc code=end

