#
# @lc app=leetcode id=1563 lang=python3
#
# [1563] Stone Game V
#

# @lc code=start
from functools import cache

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        """
        DP problem
        for each i 
        choose left: upto excluding i
        choose right: the nums after i
        the side worth most points will be discarded
        alice gets points worth the other side 

        prefix su array so we can quickly calculate the value of any subarray

        """
        n = len(stoneValue)
        prefix = [0] * (n+1)
        for i in range(1, n+1):
            prefix[i] = stoneValue[i-1] + prefix[i-1]
        
        
        @cache
        def dp(start, end):
            if start == end:
                return 0

            result = 0

            for i in range(start+1, end):
                left = prefix[i] - prefix[start]
                right = prefix[end] - prefix[i]
                if left > right:
                    #left is discarded
                    score = right + dp(i, end)
                elif left < right:
                    score = left + dp(start, i)
                else:
                    #in case of tie choose whichever is most favorable to alice
                    score = max(right + dp(i, end), left + dp(start, i))
                
                if score > result:
                    result = score
            return result
                    
                
                

        
        return dp(0, n)



        

        


        
# @lc code=end

