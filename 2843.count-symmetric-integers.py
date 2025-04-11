#
# @lc app=leetcode id=2843 lang=python3
#
# [2843]   Count Symmetric Integers
#

# @lc code=start
def is_symmetric(num):
    s = str(num)
    n = len(s)
    if n % 2 == 1:
        return False
    mid = n//2
    left_sum = sum(map(int, s[:mid]))
    right_sum = sum(map(int, s[mid:]))
    return left_sum == right_sum
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        tot = 0
        for i in range(low, high+1):
            if is_symmetric(i):
                tot += 1
        return tot
# @lc code=end

