#
# @lc app=leetcode id=2081 lang=python3
#
# [2081] Sum of k-Mirror Numbers
#

# @lc code=start
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def isPalindrome(x: int) -> bool:
            digit = list(
            )
            while x:
                x, rem = divmod(x, k)
                digit.append(rem)
            return digit == digit[::-1]

        left, count, res = 1, 0, 0
        
        while count < n:
            right = left * 10
            
            for op in [0,1]:
                for i in range(left, right):
                    if count == n:
                        break
                    combined = i
                    x = i // 10 if op == 0 else i
                    while x :
                        combined = combined * 10 + x % 10
                        x //= 10
                    if isPalindrome(combined):
                        count += 1
                        res += combined
            left = right 
        return res 
        
# @lc code=end

