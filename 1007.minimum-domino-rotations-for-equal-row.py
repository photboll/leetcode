#
# @lc app=leetcode id=1007 lang=python3
#
# [1007] Minimum Domino Rotations For Equal Row
#

# @lc code=starto
from collections import Counter
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        """
        No i misinterpreted to begin with, i thogut that it was supposed to be the sums of top and bottom to be equal
        i don't know how i got to that bpoint but i did, 
        For it to be possible there every domino needs to have the target value on it
        we can check in a single pass at each step the new domio hae atleast one value in common with the previous,
        if it does no, then it is impossible 
        """
        candidates = set((tops[0], bottoms[0]))
        n = len(tops)
        top_counts = Counter()
        bot_counts = Counter() 
        for i in range(n):
            cand_top = tops[i] 
            cand_bot = bottoms[i]
            #print(candidates)
            if cand_top in candidates and cand_bot in candidates:
                candidates = set([cand_top, cand_bot])
                top_counts[cand_top] += 1
                bot_counts[cand_bot] += 1
            elif cand_top in candidates:
                top_counts[cand_top] += 1
            elif cand_bot in candidates:
                bot_counts[cand_bot] += 1
            else:
                #the current domino have none of the candidates on it
                #no rotation on it can make it a candidate
                return -1
        
        #print(top_counts, bot_counts)
        #print(candidates)
        min_rotations = n + 1
        for target in candidates:
            #print(top_counts[target] + bot_counts[target], n)
            if top_counts[target] + bot_counts[target] >= n:
                min_rotations = min(min_rotations, n - max(top_counts[target], bot_counts[target]))
        
        if min_rotations == n+1:
            return -1
        else:
            return min_rotations
            

            
        
# @lc code=end

