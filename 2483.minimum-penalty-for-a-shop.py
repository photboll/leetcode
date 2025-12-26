#
# @lc app=leetcode id=2483 lang=python3
#
# [2483] Minimum Penalty for a Shop
#

# @lc code=start
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)

        min_penalty = 0
        min_i = 0
        penalty = 0

        for i in range(n):
            if customers[i] == "Y":
                penalty -= 1
            else:
                penalty += 1
            
            if penalty < min_penalty:
                min_i = i+1
                min_penalty = penalty
        return min_i
                

            
        
# @lc code=end

