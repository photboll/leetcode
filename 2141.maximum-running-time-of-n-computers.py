#
# @lc app=leetcode id=2141 lang=python3
#
# [2141] Maximum Running Time of N Computers
#

# @lc code=start
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        """
        since there is no time cost in switching batteries. the distribution of extra power across the extra batteries
        does not matter. 
        
        """
        batteries.sort()
        extra_power = sum(batteries[:-n])

        #Start with using the n largest batteries 
        in_use = batteries[-n:]

        #distibute the extra power among the computers 
        for i in range(n-1):

            #our remaining extra power can be distirbuted to the i+1 
            #computers whit the lowest power
            ex_power_per_comp = extra_power // (i+1)
            #will we have any power left 
            if ex_power_per_comp < in_use[i+1] - in_use[i]:
                return in_use[i] + ex_power_per_comp
            
            #perform the distribution of power
            extra_power -= (i+1) * (in_use[i+1] - in_use[i])
        
        return in_use[-1] + extra_power // n
            
        
# @lc code=end

