#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        used = [False] * len(nums)
        def backtrack(permutation):
            if len(permutation) == len(nums):
                results.append(list(permutation))
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and used[i-1]:
                    continue
                used[i] = True
                permutation.append(nums[i])
                backtrack(permutation)
                permutation.pop()
                used[i] = False
        backtrack([])
        return results
# @lc code=end

