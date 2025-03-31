#
# @lc app=leetcode id=2551 lang=python3
#
# [2551] Put Marbles in Bags
#

# @lc code=start
from functools import cache
    
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        #We need to partition the list of weights into k partitions 
        #Only the end points of each subarray affects the score 
        #Weights should be positive, 
        if k == 1:
            #only one partition, min and max will be equal
            return 0
        
        pair_sums = [weights[i] + weights[i+1] for i in range(len(weights)-1)]
        
        pair_sums.sort()
        
        best = sum(pair_sums[-(k-1):])
        
        worst = sum(pair_sums[:k-1])
        #print(best, worst, pair_sums)
        return best - worst
         
# @lc code=end

