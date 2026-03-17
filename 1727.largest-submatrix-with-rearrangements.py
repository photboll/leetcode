#
# @lc app=leetcode id=1727 lang=python3
#
# [1727] Largest Submatrix With Rearrangements
#

# @lc code=start
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        """ 
        what is the size of the contigours sequences of 1s in each column?
        WE can olnly reorder columns 
        is it optimal to be greedy?
        sort the columns in order of the longest sequence. but it must be possible that the contigus sequences are offset from each other
        1. keep the current sum of contigous ones for each column
        2. sort them and find the maximal area of a submatrix with a cornner in origo
        3. move over to the next row and repeat

        sine we sort the columns the area is easily computed as current height * (current index+1)

        """
        def max_area_sorted(heights):
            res = 0
            for i, h in enumerate(heights):
                res = max(res, 
                          h * (i+1)
                          )
            return res

        result = 0
        m = len(matrix)
        n = len(matrix[0])
        cur_heights = [0] * n

        for row in matrix:
            for i in range(n):
                if row[i] == 1:
                    cur_heights[i] += 1
                else:
                    cur_heights[i] = 0
            result = max(result, 
                         max_area_sorted(sorted(cur_heights, reverse=True)))
            #
            # print(cur_heights, result)
            
        return result

                


        
# @lc code=end

