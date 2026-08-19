#
# @lc app=leetcode id=1386 lang=python3
#
# [1386] Cinema Seat Allocation
#

# @lc code=start
from collections import defaultdict
GROUP_SIZE = 4
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        """Greedily place a family as soon as 4 availalbe seats in a row are found?"""
        left = 0b0111100000 #group is placed in [2, 3, 4, 5]
        middle = 0b0001111000 # [4,5,6,7]
        right = 0b0000011110 # [6,7,8,9]
        occupied = defaultdict(int)
        for row, col in reservedSeats:
            occupied[row] |= (1 << (col -1))

        
        #Empty rows can fit two groups
        result = (n - len(occupied)) * 2
        for bitmask in occupied.values():
            left_free = not (bitmask & left)
            right_free = not (bitmask & right)
            mid_free = not (bitmask & middle)

            if left_free and right_free:
                result += 2
            elif left_free or mid_free or right_free:
                result += 1

        return result
        
# @lc code=end

