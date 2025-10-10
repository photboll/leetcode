#
# @lc app=leetcode id=3147 lang=python3
#
# [3147] Taking Maximum Energy From the Mystic Dungeon
#

# @lc code=start
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        """
        This is similar to the jumping stairs DP problem
        or a prefix sum going backwards
        """

        n = len(energy)
        total = [-float("inf")] * n
        for i in range(n-1,-1,-1):
            #Can we jump from this position?
            if i + k < n :
                total[i] = total[i+k] + energy[i]
            
            else:
                #No, the total energy starting from this position 
                #is the energy from this wizard
                total[i] = energy[i]
        
        return max(total)
        
# @lc code=end

