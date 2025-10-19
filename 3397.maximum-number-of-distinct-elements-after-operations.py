#
# @lc app=leetcode id=3397 lang=python3
#
# [3397] Maximum Number of Distinct Elements After Operations
#

# @lc code=start
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()

        result = 0
        prev = -float("inf")

        for num in nums:
            curr = min(max(num-k , prev+1), num + k)
            if curr > prev:
                result += 1
                prev = curr
        return result
        
# @lc code=end

