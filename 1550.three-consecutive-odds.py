#
# @lc app=leetcode id=1550 lang=python3
#
# [1550] Three Consecutive Odds
#

# @lc code=start
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd_count = 0
        for num in arr:
            if num % 2 == 1:
                odd_count += 1
                if odd_count == 3:
                    return True
            else:
                odd_count = 0
                
        return False
        
# @lc code=end

