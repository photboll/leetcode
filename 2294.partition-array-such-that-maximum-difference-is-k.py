#
# @lc app=leetcode id=2294 lang=python3
#
# [2294] Partition Array Such That Maximum Difference Is K
#

# @lc code=start
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
            
        nums.sort()
        num_parts = 1
        mn = nums[0]
        for num in nums:
            if num - mn > k:
                num_parts += 1
                mn = num
        return num_parts
        
# @lc code=end

