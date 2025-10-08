#
# @lc app=leetcode id=2300 lang=python3
#
# [2300] Successful Pairs of Spells and Potions
#

# @lc code=start
import bisect
from fractions import Fraction

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        """
        Binary search the potions list to find the
        smallest potion that passess. potions[success_min]
        if potions is sorted then we know that all potions 
        """
        n = len(potions)
        potions.sort()
        res = []

        for spell in spells:
            frac = Fraction(success, spell)
            min_success = bisect.bisect_left(potions, frac)
            #print(frac, min_success)
            res.append(n - min_success)
        return res




        
# @lc code=end

