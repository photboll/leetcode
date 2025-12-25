#
# @lc app=leetcode id=3075 lang=python3
#
# [3075] Maximize Happiness of Selected Children
#

# @lc code=start
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        result = 0
        n_picks = 0
        while n_picks < k:
            val = max( happiness.pop() - n_picks, 0)
            result += val
            n_picks += 1
            if val == 0:
                return result

        return result 


        
# @lc code=end

