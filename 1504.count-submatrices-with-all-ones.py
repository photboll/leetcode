#
# @lc app=leetcode id=1504 lang=python3
#
# [1504] Count Submatrices With All Ones
#

# @lc code=start
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat) 
        n = len(mat[0])
        heights = [0] * n
        total = 0
        
        for row in mat:
            for i, val in enumerate(row):
                if val == 0:
                    heights[i] = 0
                else:
                    heights[i] += 1
            
            stack = [[-1, 0, -1]]
            for right, h in enumerate(heights):
                while stack[-1][2] >= h:
                    stack.pop()
                
                left, prev, _ = stack[-1]
                cur = prev + (right-left) * h
                stack.append([right, cur, h])
                total += cur
        
        return total

                
                
                
                

       
       
       
# @lc code=end

