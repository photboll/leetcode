#
# @lc app=leetcode id=1356 lang=python3
#
# [1356] Sort Integers by The Number of 1 Bits
#

# @lc code=start
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        arr.sort(key=lambda x: x.bit_count())
        return arr
        
# @lc code=end

