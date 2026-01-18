#
# @lc app=leetcode id=473 lang=python3
#
# [473] Matchsticks to Square
#

# @lc code=start
from functools import cache

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        """ 
        need to find 4 partitions of matchsticks which have the same sum
        total sum must be multiple of 4. is that sufficient for a solution to exist? no, example 2 is counterexample
        am i forced to consider all possible partitions?
        
        """
        n = len(matchsticks)
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        
        matchsticks.sort(reverse=True)
        target = total // 4

        @cache
        def backtrack(state, i):
            if i == n:
                return all([s == target for s in state])

            
            state = list(state)
            for part in range(len(state)):
                if state[part] + matchsticks[i] > target:
                    continue

                state[part] += matchsticks[i]
                if backtrack(tuple(state), i+1):
                    return True
                state[part] -= matchsticks[i]
                
                if state[part] == 0:
                    #exit early if it is impossible to include current stick 
                    #in any solution 
                    break

            return False

        return backtrack(tuple([0] * 4), 0)

        
# @lc code=end

