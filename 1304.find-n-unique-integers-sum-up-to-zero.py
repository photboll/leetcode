#
# @lc app=leetcode id=1304 lang=python3
#
# [1304] Find N Unique Integers Sum up to Zero
#

# @lc code=start
class Solution:
    def sumZero(self, n: int) -> List[int]:
        nums = []
        for i in range(n // 2):
            nums.append(i+1)
            nums.append(-i-1)
        
        if len(nums) < n:
            nums.append(0)
        return nums
            
        
# @lc code=end

