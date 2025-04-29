#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum = 0
        max_altitude = 0
        for num in gain:
            prefix_sum += num
            max_altitude = max(prefix_sum, max_altitude)
        return max_altitude
        
# @lc code=end

