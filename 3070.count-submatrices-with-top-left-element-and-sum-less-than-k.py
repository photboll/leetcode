#
# @lc app=leetcode id=3070 lang=python3
#
# [3070] Count Submatrices with Top-Left Element and Sum Less Than k
#

# @lc code=start
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        """  
        compute prefix sums. do i need it in 2D? or only the previos row?
        one row should be enough 
        then for each row 
        
        """
        result = 0
        m = len(grid)
        n = len(grid[0])
        #will hold the prefix column sum up to the current row
        prefix = [0] * n
        
        for r in range(m):
            cur_sum = 0
            for c in range(n):
                prefix[c] += grid[r][c]
                cur_sum += prefix[c]
                if cur_sum <= k:
                    print(r, c, cur_sum, prefix)
                    result += 1
        return result 


# @lc code=end

