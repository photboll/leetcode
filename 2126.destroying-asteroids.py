#
# @lc app=leetcode id=2126 lang=python3
#
# [2126] Destroying Asteroids
#

# @lc code=start
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()

        for asteroid in asteroids:
            if mass >= asteroid:
                mass += asteroid
            else:
                return False
                
        return True
        
# @lc code=end

