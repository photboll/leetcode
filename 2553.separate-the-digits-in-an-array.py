#
# @lc app=leetcode id=2553 lang=python3
#
# [2553] Separate the Digits in an Array
#

# @lc code=start
def int2digits(num):
    res = []
    while num > 0:
        num, rem = divmod(num, 10)
        res.append(rem)
    return res[::-1]

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            res.extend(int2digits(num))
        return res


        
# @lc code=end

