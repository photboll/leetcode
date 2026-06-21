#
# @lc app=leetcode id=1344 lang=python3
#
# [1344] Angle Between Hands of a Clock
#

# @lc code=start
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        """
        each arc 1 to 2 and so on is 30 degrees
        the hour hand is offset by 30*(60 - minutes)/60
        """
        hour %= 12
        minutes %= 60
        frac = minutes/ 60 
        mintute_deg = 360*frac
        hour_deg = 30*(hour + frac)

        print(hour_deg, mintute_deg)

        return min(
            (hour_deg - mintute_deg + 360) % 360,
            (mintute_deg - hour_deg + 360) % 360
        )
        
        
# @lc code=end

