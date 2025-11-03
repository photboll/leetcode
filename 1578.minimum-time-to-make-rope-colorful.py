#
# @lc app=leetcode id=1578 lang=python3
#
# [1578] Minimum Time to Make Rope Colorful
#

# @lc code=start
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        cur_col = colors[0]
        cur_sum = neededTime[0]
        cur_max_t = neededTime[0]

        result = 0
        for i in range(1,n):
            if cur_col == colors[i]:
                cur_sum += neededTime[i]
                cur_max_t = max(cur_max_t, neededTime[i])
            
            else:
                result += cur_sum - cur_max_t
                cur_col = colors[i]
                cur_sum = neededTime[i]
                cur_max_t = neededTime[i]
        
        result += cur_sum - cur_max_t
        return result
            

            
        
# @lc code=end

