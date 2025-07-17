#
# @lc app=leetcode id=3202 lang=python3
#
# [3202] Find the Maximum Length of Valid Subsequence II
#

# @lc code=start
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        """
        sub can start at any index
        can we use a similar approach like the k=2 case?
        the sum (mod k)of any two consecutive elements must lie in [0, k)
        The longest sub must be one these k types. 
        
        for each num we consider if we can append it to any one of the the previously seen longest of a type k
        let x be one of nums
        r = x % k
        x can extend a  
        """
        dp = [[0] * k for _ in range(k)]
        res = 0
        for num in nums:
            num %= k
            for prev in range(k):
                dp[prev][num] = dp[num][prev] + 1
                res = max(res, dp[prev][num])

        return res
        
# @lc code=end

