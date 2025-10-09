#
# @lc app=leetcode id=3494 lang=python3
#
# [3494] Find the Minimum Amount of Time to Brew Potions
#

# @lc code=start
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        """
        This seem to e scheduling problem. very similar to meeting problem 
        
        we must brew them in order, there is no room to actual move around any of the subtasks
        we should be able to simply compute the total time needed to brew a potion and then add all
        of them together 
        NO, this is wrong.
        wizard 1 can start on potion 2 before potion2 is finished.
        
        """
        n = len(skill)
        m = len(mana)


        times = [0] * n
        for j in range(m):
            cur_t = 0
            for i in range(n):
                cur_t = max(cur_t, times[i]) + skill[i] * mana[j]
            times[n-1] = cur_t

            for i in range(n-2, -1, -1):
                times[i] = times[i+1] - skill[i+1] * mana[j]

        return times[-1]







        
# @lc code=end

