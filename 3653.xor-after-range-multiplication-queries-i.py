#
# @lc app=leetcode id=3653 lang=python3
#
# [3653] XOR After Range Multiplication Queries I
#

# @lc code=start

MOD = pow(10, 9) + 7
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:

        for l, r, k, v in queries:
            idx = l
            while idx <= r:
                nums[idx] = (nums[idx] * v) % MOD
                idx += k

        
        result = 0
        for num in nums:
            result ^= num
        return result
        
# @lc code=end

