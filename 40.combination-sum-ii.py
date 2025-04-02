#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        combination = []
        candidates.sort()
        n = len(candidates)
        def backtrack(start_i, cur_sum):
            if cur_sum == target:
                results.append(list(combination))
                return
            
            for i in range(start_i, n):
                num = candidates[i]
                if cur_sum + num > target:
                    continue
                if i > start_i and candidates[i] == candidates[i-1]:
                    #skip duplicate candidates at the same recursion depth
                    continue
                
                combination.append(num)
                backtrack(i+1,cur_sum + num)
                combination.pop()

        backtrack(0, 0) 
        return results
# @lc code=end

