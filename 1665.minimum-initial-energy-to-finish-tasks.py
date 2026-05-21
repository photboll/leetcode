#
# @lc app=leetcode id=1665 lang=python3
#
# [1665] Minimum Initial Energy to Finish Tasks
#

# @lc code=start
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        """
        the sum of all actual energy is the lower bound of the answer
        binary search if it is possible to solve it with energy less than x
        is there a specific characterisitc of a taks that makes it hard to finish i.e. being the bottleneck 
        if the minimum energy is high it is better to do the task early 
        
        possible ways to order:
        1. on the minimum value 
        2. on the actual value
        3. on the difference minimum - actual 
        
        if we have one task remaining the difference of min - actual will be the energy we have left over after completion. This is essentially the quantity we want to minimize 
        minimum effort = sum of actual + excess energy 
        
        
        """

        tasks.sort(key=lambda t: t[1] - t[0])

        total = 0
        for actual, minimum in tasks:
            total = max(total + actual, minimum)
        
        return total
        
# @lc code=end

