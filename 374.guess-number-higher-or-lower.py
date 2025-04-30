#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            pick = (low+ high) // 2
            comparison = guess(pick)
            if comparison == 0:
                return pick
            elif comparison < 0:
                high = pick -1
            else:
                low = pick + 1
        
                
        
# @lc code=end

