#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        #The number of digits in n will have a great effect on the result 
        # n< 5 -> No trailing zeros 
        # n < 10 -> 1 trailing zero
        # n < 15 -> 2
        # n < 20 -> 3
        #each time we pass multiple of 5 or 10 then we get more trailing zeros 
        #How eill this chagne when we get even more digits. i.e. they are mulitples of 50 and 100
        # if it is a multple of 50 then we should add two 0s 
        # when we go from n 24 to n 25 then we need to add two 0s as well since 25=5*5
        ans = 0
        while n >= 5:
            n //= 5
            ans += n
        return ans
        
        
# @lc code=end

