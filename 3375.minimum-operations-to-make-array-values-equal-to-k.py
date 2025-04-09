#
# @lc app=leetcode id=3375 lang=python3
#
# [3375] Minimum Operations to Make Array Values Equal to K
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        unique = sorted(set(nums), reverse= True)
        if unique[-1] < k:
            return -1
        
        ops = 0
        for num in unique:
            if num > k:
                ops += 1
            else:
                break
        
        
        return ops
        
# @lc code=end

