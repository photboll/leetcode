#
# @lc app=leetcode id=2327 lang=python3
#
# [2327] Number of People Aware of a Secret
#

# @lc code=start
MOD = pow(10, 9) + 7
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        """
        dp: dp[i][j] =number of people who have known the secret for j+1 days at day i
        a key component of this problem is that the delay and forget values are the same for everyone 
        days are 1/indexed

        
        What matters on any single day is how many people who knows the secret.
        This is the same as total number of people who have ever known it - the #people who forgot
        on a new day, how many people will learn the secret?
        will it be the number of people who knew the secret delay days ago?
        on a new day, how many people will forget the secret?
        will it be the number of people who knew the secret forget days ago?
        
        
        how many people will start sharing on day i? All people who learnt it on day i-delay
        how many people will forget on day i? All people who learnt it on day i-forget
        how many people will share the secret today?
            1. people who shared it yesterday
            2. + people who will start sharing
            3. - people who will forget
        
        how many people will know the secret tomorrow?
            1. The people who know it today
            2. - the people who will forget it 
            3. + the people who share it today 
        """

        #How many people learn 
        dp = [0] * (n+1)
        total = 0
        dp[1] = 1
        
        for i in range(2, n+1):
            total = (total + dp[max(i-delay, 0)]) % MOD# new sharers
            total = (total - dp[max(i-forget, 0)]) % MOD# Remove forgotten 
            dp[i] = total

        result = 0
        for j in range(n-forget+1, n+1):
            result = (result + dp[j]) % MOD
        return result


            




        
# @lc code=end

