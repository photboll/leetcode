#
# @lc app=leetcode id=1488 lang=python3
#
# [1488] Avoid Flood in The City
#

# @lc code=start
import bisect

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [1] * len(rains)
        #Mapping from lake id to the day it was last filled 
        full_on_day = {}

        dry_days = []

        for i, lake in enumerate(rains):
            if lake == 0:
                # a dry day
                dry_days.append(i)
            else:
                # no drying action is taken this day 
                ans[i] = -1

                if lake in full_on_day:
                    #Then there is a possibiliy of flood
                    last_rain_day = full_on_day[lake]

                    pos = bisect.bisect_right(dry_days, last_rain_day)
                    
                    if pos == len(dry_days):
                        #There is no day available to dry the lake
                        #We can not avoid the flood
                        return []
                    
                    dry_day_to_use = dry_days[pos]
                    ans[dry_day_to_use] = lake
                    dry_days.pop(pos)

                full_on_day[lake] = i
        return ans 
        
        
# @lc code=end

