#
# @lc app=leetcode id=3289 lang=python3
#
# [3289] The Two Sneaky Numbers of Digitville
#

# @lc code=start
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        seen = set()
        for num in nums:
            if num in seen:
                res.append(num)
            seen.add(num)
        return res
        
# @lc code=end

