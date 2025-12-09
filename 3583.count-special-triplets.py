#
# @lc app=leetcode id=3583 lang=python3
#
# [3583] Count Special Triplets
#

# @lc code=start
from collections import Counter, defaultdict
MOD = pow(10, 9) + 7
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        freqs_prev = Counter()
        freqs_next = Counter(nums)

        
        result = 0
        for j in range(n):
            val = nums[j]
            freqs_next[val] -= 1
            result = (result + freqs_next[2*val] * freqs_prev[2*val]) % MOD
            freqs_prev[val] += 1
        return result
            

        
# @lc code=end

