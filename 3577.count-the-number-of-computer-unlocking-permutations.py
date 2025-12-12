#
# @lc app=leetcode id=3577 lang=python3
#
# [3577] Count the Number of Computer Unlocking Permutations
#

# @lc code=start
MOD = pow(10, 9) + 7
class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)

        if n <= 1:
            return 1
        
        root_val = complexity[0]

        for i in range(1, n):
            if complexity[i] <= root_val:
                return  0

        res = 1
        for i in range(2, n):
            res = (res * i) % MOD
        return res 
        
# @lc code=end

