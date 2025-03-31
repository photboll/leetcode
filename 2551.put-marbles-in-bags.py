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
        #WE should be able to find the minimum simply by negating each weight and looking for the maximum 
        @cache
        def getMaximumScore(start, k):
            #We need to consider the len(weights) choose k-1 possible split points
            #it might be possible to discard a lot of them directly 
            #Can we do it greedily?
            #print(weights, k)
            if k == 1:
                return weights[start] + weights[-1]
            
            best_score = float("-inf")
            for split_point in range(start, len(weights)-k + 1):
                cur_score = weights[start] + weights[split_point] + getMaximumScore(split_point+1, k-1)
                #print(weights, split_point, cur_score)
                best_score = max(best_score, cur_score)
            return best_score
        highest = getMaximumScore(0, k)
        weights = [-w for w in weights]
        getMaximumScore.cache_clear()
        lowest = -getMaximumScore(0, k)
        #print(highest, lowest, highest - lowest)
        
        return highest - lowest
         
# @lc code=end

