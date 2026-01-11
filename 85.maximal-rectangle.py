#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#

# @lc code=start

def largestRectangleArea(heights: List[int]) -> int:
    n = len(heights)
    left_i = [-1] * n
    right_i = [n] * n
    stack = []

    #Find the nearest index that have a height less than the current index
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        left_i[i] = stack[-1] if stack else -1
        stack.append(i)


    stack.clear()
    for i in range(n-1, -1, -1):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        right_i[i] = stack[-1] if stack else n
        stack.append(i)
    max_area = 0
    for i in range(n):
        #The currently considered rectangle
        width = right_i[i] - left_i[i] - 1
        max_area = max(max_area, heights[i] * width)
        
    return max_area

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """ 
        Dp approach. can we extend the square case to rectangle?
        that will probably be very messy.
        doing largest rectangle in histogram for each row maybe?
        """
        m = len(matrix)
        n = len(matrix[0])
        #cur row will contain the height of the column with 1s starting from the current row
        cur_row = [0] * n

        max_area = 0
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == "1":
                    cur_row[c] += 1
                else:
                    #if its not a 1. then there is no bar of 1s at this row
                    cur_row[c] = 0
            
            area = largestRectangleArea(cur_row)
            max_area = max(max_area, area)
        return max_area

            

            
        
# @lc code=end

