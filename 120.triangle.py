#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        DP: row based, we keep track of the best solution so far 
        each step can come from one of the neighbnoring steps in the row above
        
        """
        prev_row = [triangle[0][0]]
        for row in range(1, len(triangle)):
            next_row = []
            for i in range(len(triangle[row])):
                
                if i == 0:
                    #if you are on the leftmost position you must have come from the position directly above
                    next_row.append(triangle[row][i] + prev_row[i])
                elif i == len(triangle[row]) -1:
                    #if you are on the rightmost position you must have come from the poition i-1
                    next_row.append(triangle[row][i] + prev_row[i-1])
                else:
                    #You can have come from two positions, directly above or one step to the side 
                    next_row.append(triangle[row][i] + min(prev_row[i-1], prev_row[i]))
            
            prev_row = next_row

        return min(prev_row)
        
# @lc code=end

