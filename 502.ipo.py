#
# @lc app=leetcode id=502 lang=python3
#
# [502] IPO
#

# @lc code=start
from heapq import heapify, heappop, heappush
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        afforded_projects = []
        i = 0
        n = len(projects)
        for _ in range(k):
            #Add all projects which we can afford to the heap
            while i < n and projects[i][0] <= w:
                heappush(afforded_projects, -projects[i][1])#Negative profit to turn it into a max heap
                i += 1
            
            
            if len(afforded_projects) == 0:
                break
            
            #Select the most profitale of the afforded projects
            w +=  -heappop(afforded_projects)
            
        return w

            
                            
        
        
# @lc code=end

