#
# @lc app=leetcode id=1920 lang=python3
#
# [1920] Build Array from Permutation
#

# @lc code=start
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[i] += 1000 * (nums[nums[i]] % 1000)

        for i in range(n):
            nums[i] //= 1000
        return nums
class SolutionV1:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]* n
        for i in range(n):
            result[i] = nums[nums[i]]
        return result
            
        
# @lc code=end

