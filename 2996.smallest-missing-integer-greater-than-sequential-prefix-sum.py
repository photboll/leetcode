#
# @lc app=leetcode id=2996 lang=python3
#
# [2996] Smallest Missing Integer Greater Than Sequential Prefix Sum
#

# @lc code=start
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        st = set(nums)
        s = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                s += nums[i]
            else:
                break
        
        res = s
        while res in st:
            res += 1
        return res
            
            

        
# @lc code=end

