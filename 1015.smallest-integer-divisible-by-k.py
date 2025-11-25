#
# @lc app=leetcode id=1015 lang=python3
#
# [1015] Smallest Integer Divisible by K
#

# @lc code=start
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        """
        n % k == 0
        k * a == n for some integer a
        do i need to check the prime decomposition of n?
        seems like that would be 
        we should be able to build a table mod k
        dp = []
        dp[a] = (dp[a-1] * 10 + 1) % K
        if the generating function for dp becomes a cycle wihtout
        """
        seen = set()
        if k == 1:
            return 1

        n = 1
        i = 1
        while n not in seen:
            seen.add(n)
            n = ((10 * n) + 1 ) % k
            #print(n)
            i += 1
            if n == 0:
                return i
        return -1

        
# @lc code=end

