#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = set()
        combination = []
        def backtrack(i, prev_num, sum):
            if i == k and sum == n:
                result.add(tuple(combination))
                return

            for num in range(prev_num+1, 10):
                combination.append(num)
                backtrack(i+1, num, sum+num)
                combination.pop()
        
        backtrack(0, 0, 0)
        return list(result)
        
# @lc code=end

