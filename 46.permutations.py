#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(permutation, visited):
            if len(permutation) == len(nums):
                result.append(permutation[:])
                return
            
            for num in nums:
                if num not in visited:
                    permutation.append(num)
                    visited.add(num)
                    backtrack(permutation, visited) 
                    permutation.pop()
                    visited.remove(num)
            
        backtrack([], set())
        return result
# @lc code=end

