#
# @lc app=leetcode id=2147 lang=python3
#
# [2147] Number of Ways to Divide a Long Corridor
#

# @lc code=start
MOD = pow(10, 9) + 7
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        """
        after we have seen two chairs, we can place a divider at any point 
        before the next chair.
        divide the corridor into segments of two chairs each 
        
        we only care about the positions of the seats 
        """
        n = len(corridor)
        seat_positions = []

        for i, char in enumerate(corridor):
            if char == "S":
                seat_positions.append(i)
                
        #We have to have two seats in each segment
        #any other arrangement is invalid
        if len(seat_positions) % 2 == 1 or len(seat_positions) == 0:
            return 0

        result =1
        for i in range(2, len(seat_positions), 2):
            #all positions between seats are planters 
            num_planters = seat_positions[i] - seat_positions[i-1]
            
            result = (result * num_planters) % MOD
        return result

            
        
# @lc code=end

