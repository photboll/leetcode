# @lc app=leetcode id=1385 slug=find-the-distance-value-between-two-arrays lang=python3
#
# [1385] Find the Distance Value Between Two Arrays
# Difficulty: Easy
# Tags: Array, Two Pointers, Binary Search, Sorting
# URL: https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
#
# @lc code=start
class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = 0
        for x in arr1:
            if all(abs(x - y) > d for y in arr2):
                count += 1

        return count 

        

# @lc code=end
