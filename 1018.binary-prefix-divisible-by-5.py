#
# @lc app=leetcode id=1018 lang=python3
#
# [1018] Binary Prefix Divisible By 5
#

# @lc code=start
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        x = 0
        result = [        ]
        for bit in nums:
            x = ((x << 1) + bit) % 5
            result.append(x==0)
        return result
class SolutionV1:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        x = 0
        result = []
        for bit in nums:
            x |= bit
            result.append(x % 5 == 0)
            x = (x << 1)

        return result
        
# @lc code=end

