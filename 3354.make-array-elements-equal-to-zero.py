#
# @lc app=leetcode id=3354 lang=python3
#
# [3354] Make Array Elements Equal to Zero
#

# @lc code=start
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        prefix = 0
        count = 0
        tot = sum(nums)
        for num in nums:
            prefix += num
            if num == 0:
                count += 2*(2*prefix == tot)
                count += (abs(2*prefix-tot) == 1)
        return count 
        
# @lc code=end

