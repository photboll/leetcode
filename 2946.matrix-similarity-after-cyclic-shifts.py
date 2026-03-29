#
# @lc app=leetcode id=2946 lang=python3
#
# [2946] Matrix Similarity After Cyclic Shifts
#

# @lc code=start
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        """
        every row needs must be cycled to it self 
        
        """

        def cycles_to_self(row, k ):
            n = len(row)
            for i in range(n):
                if row[i] != row[(i +k + n) % n]:
                    return False
            return True

        for i, row in enumerate(mat): 
            if i % 2 == 0 and not cycles_to_self(row, -k):
                return False
            elif i % 2 == 1 and not cycles_to_self(row, k):
                return False
        return True
            

            
        
# @lc code=end

