#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#

# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        result = []
        for asteroid in asteroids:
            if asteroid >= 0:
                stack.append(asteroid)
                continue
            
            while stack:
                magnitude = abs(asteroid)
                if magnitude < stack[-1]:
                    #this asteriod will be destroyed
                    asteroid = None
                    break
                elif magnitude == stack[-1]:
                    #both asteroids will be destroyed
                    asteroid = None
                    stack.pop()
                    break
                else:
                    #The asteroid on the stack gets destroyed
                    stack.pop()

            if len(stack) == 0 and asteroid is not None:
                #asteroid is moving left and it won't collide with anything
                result.append(asteroid)
        
        result.extend(stack)
        return result
        
# @lc code=end

