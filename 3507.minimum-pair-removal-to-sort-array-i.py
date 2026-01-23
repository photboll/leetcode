#
# @lc app=leetcode id=3507 lang=python3
#
# [3507] Minimum Pair Removal to Sort Array I
#

# @lc code=start
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count = 0

        while len(nums) > 1:
            isAscending = True
            min_sum = float("inf")
            targetIndex = -1

            for i in range(len(nums) -1 ):
                pair_sum = nums[i] + nums[i+1]

                if nums[i] > nums[i+1]:
                    isAscending = False
                
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    targetIndex = i

            if isAscending:
                break

            count += 1
            nums[targetIndex] = min_sum
            nums.pop(targetIndex+1)

        return count 

        
# @lc code=end

