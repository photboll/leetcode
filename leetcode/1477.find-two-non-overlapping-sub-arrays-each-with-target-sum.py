# @lc app=leetcode id=1477 slug=find-two-non-overlapping-sub-arrays-each-with-target-sum lang=python3
#
# [1477] Find Two Non-overlapping Sub-arrays Each With Target Sum
# Difficulty: Medium
# Tags: Array, Hash Table, Binary Search, Dynamic Programming, Sliding Window
# URL: https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/
#
# @lc code=start
class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr) 
        result = n+1
        total = 0

        dp = [n] * (n+1)
        l = 0
        for r, val in enumerate(arr):
            total += val

            while total > target:
                total -= arr[l]
                l += 1
            
            dp[r+1] = dp[r]
            if total == target:
                result = min(result, r - l + 1 +dp[l])
                dp[r+1] = min(dp[r], r - l + 1)

        return -1 if result == n+1 else result


            
        

# @lc code=end
