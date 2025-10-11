#
# @lc app=leetcode id=3186 lang=python3
#
# [3186] Maximum Total Damage With Spell Casting
#

# @lc code=start

from collections import Counter
import bisect

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        freqs = Counter(power)
        spells = list(set(power))
        spells.sort()

        n = len(spells)
        dp = [0] * n
        dp[0] = freqs[spells[0]]*spells[0]

        for i in range(1, n):
            #Total Damage if we decide to use spells[i]
            tot_damage = freqs[spells[i]] * spells[i]
            #How many spells will be skipped if we take the current one
            prev = bisect.bisect_right(spells, spells[i] - 3, 0, i) - 1 
            if prev >= 0:
                tot_damage += dp[prev]
            
            #we can either skip the current spells[i] or use it
            dp[i] = max(dp[i-1], tot_damage)

        return dp[-1]


            
            

        


    
        
        

        
# @lc code=end

