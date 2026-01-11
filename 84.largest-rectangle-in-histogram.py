#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """  
        similar to trapping rainwater problem?
        
        going from left to right. what is the largest rectangle with the current height?
        what is the largest rectangle with this column as its right edge?
        if this is the right edge, then we are interested in when and where 
        when we move passed a short bar, we should be able discard data from earlier
        at every height were do we find the leftmost bar?
        any bar that is greater than or equal 
        
        heights = [2,1,5,6,2,3]
        area = h * w
        suppose we are at index 3 (height 6).
        a rectangle of height 1 will have left edge at 0
        a rectangle of height 5 will have left edge at 2
        a rectangle of height 6 will have left edge at 3
        a rectangle of height 2 is not necessary to consider because we know its left edge will be at 2,
        where we already know of a better solution. 
        
        the logic for emptying the stack.
        evey time we see a lower bar we can prune the stack
        we are at index 4 (height 2).
        a rectangle of height 1 will have left edge at 0
        a rectangle of height 5 not possible becuase current height < 5 it is capped at the current height 
        stack after
        [(0, 1) (2, 2)]
        this is messy. I think trapping rain water approach is better
        """

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
        #print(left_i)
        #print(right_i)
        max_area = 0
        for i in range(n):
            #The currently considered rectangle
            width = right_i[i] - left_i[i] - 1
            max_area = max(max_area, heights[i] * width)
            
        return max_area
            

        
# @lc code=end

