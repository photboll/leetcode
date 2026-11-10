# @lc app=leetcode id=3693 slug=climbing-stairs-ii lang=python3
#
# [3693] Climbing Stairs II
# Difficulty: Medium
# Tags: Array, Dynamic Programming
# URL: https://leetcode.com/problems/climbing-stairs-ii/
#
# @lc code=start

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0] *(n +1)

        for i in range(1, n+1):
            dp[i] = float("inf")
            for d in range(1, 4):
                if i - d >= 0:
                    dp[i] = min(
                        dp[i],
                        dp[i-d] + costs[i-1] + d*d
                    )

        return dp[-1]
                        
                    
            
        

# @lc code=end
