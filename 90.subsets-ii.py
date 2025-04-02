#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        subset = []
        def backtrack(start_i):
            results.append(list(subset))
            
            for i in range(start_i, len(nums)):
                if i> start_i and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                backtrack(i+1)
                subset.pop()
            
        backtrack(0)
        return results       
# @lc code=end

