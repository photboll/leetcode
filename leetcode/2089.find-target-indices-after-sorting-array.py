# @lc app=leetcode id=2089 slug=find-target-indices-after-sorting-array lang=python3
#
# [2089] Find Target Indices After Sorting Array
# Difficulty: Easy
# Tags: Array, Binary Search, Sorting
# URL: https://leetcode.com/problems/find-target-indices-after-sorting-array/
#
# @lc code=start
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        return [i for i, num in enumerate(nums) if num == target]
        

# @lc code=end
