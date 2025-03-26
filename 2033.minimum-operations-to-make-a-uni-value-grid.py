#
# @lc app=leetcode id=2033 lang=python3
#
# [2033] Minimum Operations to Make a Uni-Value Grid
#

# @lc code=start
def flattenMatrix(matrix):
    for i in  range(1, len(matrix)):
        matrix[0].extend(matrix[i])
    return matrix[0]
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flattened = flattenMatrix(grid)
        flattened.sort()
        print(flattened)
        #The least amount of operattion is if the target number is in the middle of the span
        #So the target should be one of the middle values in the flattened array
        # each number in the grid needs to have the same remainder when divided by x
        #else no adding or subtracting of x can ever make them equal 
        #To count the number of opearations we need to know the target number 
        totalOperations = 0
        
        #Determine whihc is the target number
        #Or is it even simpler, just choose the number closest to thee middle of the array.
        #No, that can't be it since the range may be very lopsided r.g. [2, 4, 6, 8, 20]
        #The number closest to the average would be (20- 2)/2 = 9 -> 8
        #but choosing 6 as the target would be better, 
        median = flattened[len(flattened)// 2]
        remainder = median % x
        for num in flattened:
            if num % x != remainder:
                return -1
            
            totalOperations += (abs(median - num) // x)
        
        
        
        return totalOperations 
        
# @lc code=end

