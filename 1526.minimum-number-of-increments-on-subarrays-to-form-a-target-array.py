#
# @lc app=leetcode id=1526 lang=python3
#
# [1526] Minimum Number of Increments on Subarrays to Form a Target Array
#

# @lc code=start
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)

        res = target[0]
        for i in range(1, n):
            res += max(target[i] - target[i-1], 0)
        return res 

        
# @lc code=end

