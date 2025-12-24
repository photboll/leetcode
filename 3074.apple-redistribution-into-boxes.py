#
# @lc app=leetcode id=3074 lang=python3
#
# [3074] Apple Redistribution into Boxes
#

# @lc code=start
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        apples = sum(apple)
        res = 0

        for box in capacity:
            apples -= box
            res += 1
            if apples <= 0:
                return res
        return -1
        
# @lc code=end

