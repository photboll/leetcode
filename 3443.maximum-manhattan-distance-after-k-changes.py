#
# @lc app=leetcode id=3443 lang=python3
#
# [3443] Maximum Manhattan Distance After K Changes
#

# @lc code=start
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        lat = 0
        long = 0
        
        result = 0
        n = len(s)
        for i in range(n):
            match s[i]:
                case "N": lat += 1
                case "S": lat -= 1
                case "E": long += 1
                case "W": long -= 1
            
            result = max(result, min(abs(lat) + abs(long) + k *2, i+1))
        return result
# @lc code=end

