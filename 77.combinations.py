#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n+1))
        result = []       
        def backtrack(start, combination):
            if len(combination) == k:
                result.append(combination[:])
                return 
            for i in range(start, len(nums)):
                combination.append(nums[i])
                backtrack(i +1, combination)
                combination.pop()

        backtrack(0, [])
        return result
# @lc code=end

