#
# @lc app=leetcode id=3633 lang=python3
#
# [3633] Earliest Finish Time for Land and Water Rides I
#

# @lc code=start
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        res = float("inf")
        
        for ls, ld in zip(landStartTime, landDuration):
            le = ls + ld
            for ws, wd in zip(waterStartTime, waterDuration):
                we = ws + wd
                #first land then water
                land_water = max(le, ws) + wd
                #first water then land
                water_land = max(we, ls) + ld
                res = min(res, 
                    land_water,
                    water_land
                            )
        return res 


                

        
# @lc code=end

