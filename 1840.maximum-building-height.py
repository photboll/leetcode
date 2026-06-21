#
# @lc app=leetcode id=1840 lang=python3
#
# [1840] Maximum Building Height
#

# @lc code=start
class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1,0])
        restrictions.append([n, n-1])
        restrictions.sort()

        n = len(restrictions)

        
        for i in range(1, n):
            dist = restrictions[i][0] - restrictions[i-1][0]
        
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i-1][1] + dist
            )
        
        
        for i in range(n-2, -1,-1):
            dist = restrictions[i+1][0] - restrictions[i][0]
        
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i+1][1] + dist
            )
        
        
        result = 0

        for i in range(1, n):
            x1, h1 = restrictions[i-1]
            x2, h2 = restrictions[i]
            
            dist = x2 -x1

            peak = max(h1, h2) + (
                dist - abs(h1-h2)
            )// 2

            result = max(result, peak)
        
        return result 
        
# @lc code=end

