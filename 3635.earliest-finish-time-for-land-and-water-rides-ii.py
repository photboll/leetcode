#
# @lc app=leetcode id=3635 lang=python3
#
# [3635] Earliest Finish Time for Land and Water Rides II
#

# @lc code=start
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def earliestFinish(start1, duration1, start2, duration2):
            # land water 
            minle = float("inf")
            for ls, ld in zip(start1, duration1):
                le = ls + ld
                minle = min(minle, le)

            finish = float("inf")
            for ws , wd in zip(start2, duration2):
                finish = (min(finish, max(ws, minle) + wd ))
            return finish
        
        land_water = earliestFinish(landStartTime, landDuration, waterStartTime, waterDuration)

        water_land = earliestFinish(waterStartTime, waterDuration, landStartTime, landDuration)

        return min(land_water, water_land)

            

        
# @lc code=end

