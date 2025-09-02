#
# @lc app=leetcode id=3025 lang=python3
#
# [3025] Find the Number of Ways to Place People I
#

# @lc code=start
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        """
        sweep line algorithm
        we sort the points in order of decreasing X value 
        """
        n = len(points)
        points.sort(key=lambda p: (-p[0], p[1]))

        total = 0
        #The lower left corner of our rectangle
        for i in range(n-1):
            #y represents the sweeping line 
            #Initailly set to the max value 
            y = 1 << 31
            #The upper right corner of our rectangle
            for j in range(i+1, n):
                #the j point have to be above i and below the sweep line
                #to be considered a valid ordering
                if y > points[j][1] >= points[i][1]:
                    total += 1
                    y = points[j][1]

        return total   

                

                
        
        
# @lc code=end

