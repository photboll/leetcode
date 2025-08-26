#
# @lc app=leetcode id=3000 lang=python3
#
# [3000] Maximum Area of Longest Diagonal Rectangle
#

# @lc code=start
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag = -1
        max_area = 0
        
        for i in range(len(dimensions)):
            length = dimensions[i][0]
            width = dimensions[i][1]
            diag2 = width**2 + length**2
            if diag2 > max_diag:
                max_area = width * length
                max_diag = diag2
            elif diag2 == max_diag:
                max_area = max(width*length, max_area)
                    
        return max_area
                
        
# @lc code=end

