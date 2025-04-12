#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        digits = []
        if x < 0:
            return False
        while x > 0:
            x, digit = divmod(x, 10)
            digits.append(digit)
        n = len(digits)
        for i in range(n//2):
            if digits[i] != digits[n-1-i]:
                return False
        return True
        
# @lc code=end

