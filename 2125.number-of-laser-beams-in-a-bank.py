#
# @lc app=leetcode id=2125 lang=python3
#
# [2125] Number of Laser Beams in a Bank
#

# @lc code=start
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        """
        First i though this would be a geometry puzzle.
        But condition two reduces this task to a much simpler problem. I first interpreted the condition as no secuity device in direct line of sight of an additonal
        any seciruty device on row1 will have a 
        we can always consider two rows at time 
        
        1. pre process each row by counting the number of devices.
        2. for each row with any devices
        2a. the number of beams between the current row and the previous row is 
        2b. devices[row1] * devices[row2]
        
        """
        m = len(bank)
        n = len(bank[0])
        result = 0
        prev_count = 0
        
        for i in range(m):
            curr_count = 0
            for j in range(n):
                if bank[i][j] == "1":
                    curr_count += 1
            
            if curr_count > 0:
                result += curr_count * prev_count
                prev_count = curr_count
        
        return result

        
# @lc code=end

