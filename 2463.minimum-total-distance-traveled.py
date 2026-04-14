#
# @lc app=leetcode id=2463 lang=python3
#
# [2463] Minimum Total Distance Traveled
#

# @lc code=start
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        """
        we need to find an assignment of robots to factories that minimzes the distance traveled
        the time element is irrelevant 
        
        unpack the factory. so  a factory with limit k is represented as k factories at that position 
        then we just need to map each robot to one factory

        
        We have i robots assigned to j factories (optimally). We want to add another factory, how can the optimally solution change
        1. the last robot is closer to the new factory than the previous one.
        2. new factory is further away, so we are already at the optimum.
        
        
        
        """
        robot.sort()
        factory.sort(key=lambda x:x[0])
        factories = []

        #unpack factories 
        for f in factory:
            factories.extend([f[0]] * f[1])
            
        m = len(robot)
        n = len(factories)
            
        dp = [[float("inf")] * n for _ in range(m)]
        #base case,
        dp[0][0] = abs(robot[0] -factories[0])
        for j in range(1, n):
            dp[0][j] = min(dp[0][j-1], abs(robot[0] - factories[j]))

        #each factory 
        for j in range(1, n):
            for i in range(1, m):
                if j < i:
                    continue
                #option 1 skip current factory
                #option 2: assign current robot to this factory. 
                dp[i][j] = min(dp[i][j-1],
                               dp[i-1][j-1] + abs(robot[i] - factories[j]))
        
        return dp[-1][-1]

                               

                

        
        
        
# @lc code=end

