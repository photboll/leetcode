#
# @lc app=leetcode id=3578 lang=python3
#
# [3578] Count Partitions With Max-Min Difference at Most K
#

# @lc code=start
from sortedcontainers import SortedList
from functools import cache
MOD = pow(10, 9) + 7
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * (n+1)
        prefix = [0] * (n+1)
        count = SortedList()

        dp[0] = 1
        prefix[0] = 1

        l = 0
        for r in range(n):
            count.add(nums[r])
            #Shrink the window if we exceed the bounds
            while l <= r and count[-1] - count[0] > k:
                count.remove(nums[l])
                l += 1
            
            dp[r+1] = (prefix[r] - (prefix[l-1] if l > 0 else 0)) % MOD
            prefix[r+1] = (prefix[r] + dp[r+1]) % MOD

        return dp[n]
        
class SolutionDP:
    def countPartitions(self, nums: List[int], k: int) -> int:
        """
        dp or sliding window with prefix sum problem)
        
        top down dp probably the easiest approach 
        [9,4,1,3,7], k = 4
        
        dp(0):
        [9 | 4,1,3,7], the only valid partition at most k apart is one
        second level 
        [9|4|1,3,7]
        [9|4,1|3,7]
        [9|4,1,3|7]
        third level
        [9|4|1|3,7]
        [9|4|1,3|7]
        4th level
        [9|4|1|3,7|]
        [9|4|1,3,7]

        its not possible to reach the end of the array with an invalid partition.
        since we can always make single element partitions which are within the constraints
        """
        n = len(nums)
        @cache
        def dp(i):
            #i is the current position in nums
            #if we have reached the end of nums
            #then we have found a valid partition
            if i >= n:
                return 1

            #we need to check every valid partition point starting from i
            mn = nums[i]
            mx = nums[i]
            tot_parts = 0
            while i < n and mx - mn <= k:
                i += 1
                tot_parts = (tot_parts + dp(i)) % MOD
                if i < n :
                    mn = min(mn, nums[i])
                    mx = max(mx, nums[i])
            
            return tot_parts

        return dp(0)
                

                
                


        
        
# @lc code=end

