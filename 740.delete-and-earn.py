#
# @lc app=leetcode id=740 lang=python3
#
# [740] Delete and Earn
#

# @lc code=start
from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        unique_nums = sorted(count.keys())
        
        prev = 0
        curr = 0
        
        for i in range(len(unique_nums)):
            points = unique_nums[i] * count[unique_nums[i]]
            if i > 0 and unique_nums[i] == unique_nums[i-1] +1:
                prev, curr = curr, max(curr, prev + points)
            else:
                prev, curr = curr, curr + points
        return curr
from functools import cache
class SolutionV1:
    def deleteAndEarn(self, nums: List[int]) -> int:
        #If we only have single number we should take it 
        nums.sort()

        @cache
        def dp(end)-> int :
            if end < 0:
                return 0
            elif end == 0:
                return nums[end] 
            
            cur_points = 0
            i = end 
            while i >= 0 and nums[i] == nums[end]:
                cur_points += nums[i]
                i -=1
            idx_if_not_chosen = i
            while i >= 0 and nums[i] == nums[end] -1:
                #If nums[end] is chosen then all nums[end] -1 need to be skipped 
                #nums[end] + 1 will alwys be skipped since nums are sorted
                i -= 1
            return max(
                cur_points + dp(i),#Take nums[end]
                dp(idx_if_not_chosen) #Skip nums[end]
            )
            
        
        return dp(len(nums) -1)
# @lc code=end

