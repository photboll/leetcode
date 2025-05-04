#
# @lc app=leetcode id=1128 lang=python3
#
# [1128] Number of Equivalent Domino Pairs
#

# @lc code=start
from collections import Counter
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        """
        for each domino:
            make sure that it is in standard representiation, i will choose in ascending order
            have we seen this one before? check counter
            add to total number of possible pairs 
            add it to the counter
        """
        counts = Counter()
        total = 0
        for dom in dominoes:
            std_dom = tuple(sorted(dom))
            total += counts[std_dom]
            counts[std_dom] += 1
        return total

        
# @lc code=end

