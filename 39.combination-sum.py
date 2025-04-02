#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        combination = []
        n = len(candidates)
        def backtrack(start_i, cur_sum):
            if cur_sum == target:
                results.append(combination[:])
                return
            elif cur_sum > target:
                #Negative integers are not allowed in the candidates, so when we move passed the target we can;t go back
                return
            
            for i in range(start_i, n):
                combination.append(candidates[i])
                backtrack(i,cur_sum + candidates[i])
                combination.pop()

        backtrack(0, 0) 
        return results
# @lc code=end

