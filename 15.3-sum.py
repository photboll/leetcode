#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        n = len(nums)
        for i in range(len(nums)):
            if i> 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            left = i +1
            right = n-1
            while left < right:
                if nums[left] == nums[left-1] or (right < n-1 and nums[right] == nums[right+1]):
                    continue
                cur_sum = nums[left] + nums[right]
                if cur_sum == target:
                    result.append((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif cur_sum < target:
                    left += 1
                else:
                    right -= 1
        return result
        
# @lc code=end

