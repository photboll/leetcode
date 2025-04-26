#
# @lc app=leetcode id=1679 lang=python3
#
# [1679] Max Number of K-Sum Pairs
#

# @lc code=start
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left, right = 0, n-1
        numOps = 0
        while left < right:
            cur_sum = nums[left] + nums[right]
            if cur_sum > k:
                right -= 1
            elif cur_sum < k:
                left +=1
            else:
                numOps += 1
                left += 1
                right -=1
        return numOps

        
# @lc code=end

