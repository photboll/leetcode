# @lc app=leetcode id=3551 slug=minimum-swaps-to-sort-by-digit-sum lang=python3
#
# [3551] Minimum Swaps to Sort by Digit Sum
# Difficulty: Medium
# Tags: Array, Hash Table, Sorting
# URL: https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/
#
# @lc code=start
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        def digit_sum(x):
            res = 0
            while x > 0:
                x, digit = divmod(x, 10)
                res += digit
            return res
        
        arr = [(digit_sum(num), num, i) for i, num in enumerate(nums)]
        arr.sort()
        #print(arr)

        visited = [False] * n
        cycles = 0

        for i in range(n):
            if not visited[i]:
                cycles += 1
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = arr[j][2]
        return n - cycles



        

# @lc code=end
