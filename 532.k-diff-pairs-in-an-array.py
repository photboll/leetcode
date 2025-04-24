#
# @lc app=leetcode id=532 lang=python3
#
# [532] K-diff Pairs in an Array
#

# @lc code=start
from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        kdiff_pairs = set()
        seen = set()
        for  num in nums:
            if num + k in seen:
                kdiff_pairs.add((num, num+k))
            if num - k in seen:
                kdiff_pairs.add((num -k, num))
            
            seen.add(num)
        return len(kdiff_pairs) 
        
        
# @lc code=end

