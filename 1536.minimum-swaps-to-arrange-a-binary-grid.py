#
# @lc app=leetcode id=1536 lang=python3
#
# [1536] Minimum Swaps to Arrange a Binary Grid
#

# @lc code=start
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        """  
        We need to know the rightmost 1 in each row
        in the case were we have multiple rows that can take position, which is preferable ?
        - the one with lowest reightmost 1
        - the row closest to the current 
        
        How do we minimze the number of swaps?
        
        """
        #find the rightmost 1 for each row
        n = len(grid)
        rightmost = [-1] * n
        for i in range(n):
            for j in range(n-1, -1, -1):
                if grid[i][j] == 1:
                    rightmost[i] = j
                    break
        
        
        #simulate moving it to the correct position 
        count = 0
        for i in range(n):
            if (rightmost[i] <= i): continue# does not need to be moved
            j = i+1
            while j < n and rightmost[j] > i:
                j +=1 
            
            if j == n :
                return -1
            
            while j > i:
                rightmost[j-1], rightmost[j] = rightmost[j], rightmost[j-1]
                count += 1
                j -= 1
        
        return count 

            
        
        
        
            
        
# @lc code=end

