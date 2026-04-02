#
# @lc app=leetcode id=2751 lang=python3
#
# [2751] Robot Collisions
#

# @lc code=start
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        """
        Robots at the edges moving away from the middle will collide and take damage 
        
        each robot have 4 attributes 
        (current_position, health, direction, name) 
        the name is the index in the original arrays 
        a result array
        
        sort all robots based on their position 
        
        a stack to keep track of robots to the left of the current position that are moving right 
        Process the positions in order.
        consider the robot at the current position. 
        if it moves right.
            then add it to the stack of surviving robots unchanged
        if it moves left.
            pop the rightmoving stack and collide the robots. keep popping until empty or right moving robot dies
            if the stack becomes empty move the right moving robot to the result array 
            
            
        keep in mind that all robots move during the process. Though we do not need to keep track of the absolute position or the time. We only care about the health at the end   
        """
        n = len(positions)
        robots = [[i, positions[i], healths[i], directions[i]] for i in range(n)]
        robots.sort(key=lambda x: x[1])
        survivors = []
        #stack_r will hold processed robots that are moving right
        stack_r = []

        for robot in robots:
            if robot[3] == "R":
                stack_r.append(robot)
                continue

            #The current robot is moving left
            while stack_r and robot[2]> 0:# current robot have health remaining
                if stack_r[-1][2] > robot[2]: # right moving robot wins
                    stack_r[-1][2] -= 1
                    robot[2] = 0 # left moving robot is dead
                elif stack_r[-1][2] == robot[2]:#Both robots die
                    stack_r.pop()
                    robot[2] = 0
                else:
                    #left moving robot wins
                    stack_r.pop()
                    robot[2] -= 1
            
            if robot[2] > 0:
                #left moving robot have survived all possible oppnents
                survivors.append(robot)
        
        #move the surviving robots from stack_r to survivors
        survivors.extend(stack_r)
        
        #move them back to their starting order
        survivors.sort(key= lambda x: x[0])
        return [s[2] for s in survivors]


            


        


        
# @lc code=end

