#
# @lc app=leetcode id=2840 lang=python3
#
# [2840] Check if Strings Can be Made Equal With Operations II
#

# @lc code=start
from collections import Counter

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        """
        the difference must always be even. i.e. a multiple of 2
        so all chars on even indices can be swapped with freely with other
        and all chars on odd indices can be swapped freely with each other
        """
        def check(start_i, step_size=2):
            freqs = Counter([c for c in s1[start_i::step_size]])
            for c in s2[start_i::step_size]:
                freqs[c] -= 1
            
            for v in freqs.values():
                if v != 0:
                    return False
            return True
        
        return check(0) and check(1)
        
        
            
        

        
        
        
# @lc code=end

