#
# @lc app=leetcode id=2578 lang=python3
#
# [2578] Split With Minimum Sum
#

# @lc code=start
class Solution:
    def splitNum(self, num: int) -> int:
        chars = [c for c in str(num)]
        chars.sort()
        num1 = []
        num2 = []
        for i, c in enumerate(chars[::-1]):
            if i % 2 == 0:
                num1.append(c)
            else:
                num2.append(c)
        return int("".join(num1[::-1])) + int("".join(num2[::-1]))        

# @lc code=end

