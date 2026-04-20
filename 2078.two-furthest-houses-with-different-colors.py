#
# @lc app=leetcode id=2078 lang=python3
#
# [2078] Two Furthest Houses With Different Colors
#

# @lc code=start
class Solution:
    def maxDistance(self, colors: List[int]) -> int:

        prev = {}
        first = {}
        for i, color in enumerate(colors):
            prev[color] = i
            if color not in first:
                first[color] = i
        
        result = 0
        for c1 in prev:
            for c2 in first:
                if c1 == c2:#colors must be different
                    continue

                result = max(result,
                             abs(prev[c1] - first[c2]))

        return result

                

                
            
        
# @lc code=end

