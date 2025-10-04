#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        res = 0
        while l < r:
            area = (r-l)
            if height[l] < height[r]:
                area *= height[l]
                l += 1
                
            else:
                area *= height[r]
                r -= 1
            res = max(area, res)
        return res

        
# @lc code=end

