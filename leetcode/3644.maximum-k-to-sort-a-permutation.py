# @lc app=leetcode id=3644 slug=maximum-k-to-sort-a-permutation lang=python3
#
# [3644] Maximum K to Sort a Permutation
# Difficulty: Medium
# Tags: Array, Bit Manipulation
# URL: https://leetcode.com/problems/maximum-k-to-sort-a-permutation/
#
# @lc code=start
class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        sort = sorted(nums)
        k = (1 << 32) -1

        for i in range(n):
            if nums[i] != sort[i]:
                k = k & nums[i]
        if k < n:
            return k
        
        return 0
                

        

# @lc code=end
