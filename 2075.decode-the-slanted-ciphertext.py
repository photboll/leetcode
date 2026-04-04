#
# @lc app=leetcode id=2075 lang=python3
#
# [2075] Decode the Slanted Ciphertext
#

# @lc code=start
class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        """
        
        we can fit rows number of chars on each level
        len(encodedText) // rows should give the number of columns 
        """
        n = len(encodedText)
        cols = n // rows
        #print(rows, cols, n)
        grid = [encodedText[r*cols:(r+1)*cols] for r in range(rows)]

        result = []
        for c in range(cols):
            i = 0
            j = c
            while i < rows and j < cols:
                result.append(grid[i][j])
                i += 1
                j += 1
        
        #print(grid)
        return "".join(result).rstrip()
            


        
# @lc code=end

