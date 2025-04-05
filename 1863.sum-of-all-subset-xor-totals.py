#
# @lc app=leetcode id=1863 lang=python3
#
# [1863] Sum of All Subset XOR Totals
#

# @lc code=start
from itertools import chain, combinations
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        def powerset(iterable):
            s = list(iterable)
            return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
            
        for subset in powerset(nums):
            total = 0
            for num in subset:
                total ^= num
            result += total
        return result
        
# @lc code=end

