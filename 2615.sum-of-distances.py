#
# @lc app=leetcode id=2615 lang=python3
#
# [2615] Sum of Distances
#

# @lc code=start
from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        num2js = defaultdict(list)
        result = [0] * len(nums)

        for i, num in enumerate(nums):
            num2js[num].append(i)

        for indices in num2js.values():
            total = sum(indices)
            prefix = 0
            n = len(indices)
            for i, idx in enumerate(indices):
                result[idx] = total - prefix * 2 + idx * (2*i - n)
                prefix += idx

        return result

class SolutionTLE:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num2j = defaultdict(list)
        result = [0] * len(nums)

        for i, num in enumerate(nums):
            num2j[num].append(i)

        for i, num in enumerate(nums):
            for j in num2j[num]:
                result[i] += abs(j-i)
        #print(num2j)
        return result
        
# @lc code=end

