#
# @lc app=leetcode id=3731 lang=python3
#
# [3731] Find Missing Elements
#

# @lc code=start
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mn = min(nums)
        mx = max(nums)
        present = set(nums)
        result = []

        for num in range(mn, mx):
            if num not in present:
                result.append(num)
        return result
        
            
        
# @lc code=end

