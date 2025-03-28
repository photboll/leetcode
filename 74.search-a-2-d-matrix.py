#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #We will convert it so that it acts as if it was a view of the flattened array insted
        def oneToTwoD(pos):
            return divmod(pos, len(matrix[0]))
        
        def towToOneD(i, j):
            return i * len(matrix[0]) + j
        
        #Then procced with normal binary search and jsut convert between the indexing types 
        
        low = 0
        high = towToOneD(len(matrix) - 1, len(matrix[0]) - 1)

        while low <= high:
            mid = low + (high - low) // 2
            i, j = oneToTwoD(mid)
            curVal = matrix[i][j]
            
            if curVal == target:
                return True
            elif curVal < target:
                low = mid + 1
            else:
                high = mid - 1
            
        return False
# @lc code=end

