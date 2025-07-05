#
# @lc app=leetcode id=1394 lang=python3
#
# [1394] Find Lucky Integer in an Array
#

# @lc code=start
from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = -1
        freqs = Counter(arr)
        for k in freqs:
            if k == freqs[k] and k > res:
                res = k
        return res
        
# @lc code=end

