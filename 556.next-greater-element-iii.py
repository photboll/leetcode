#
# @lc app=leetcode id=556 lang=python3
#
# [556] Next Greater Element III
#

# @lc code=start
MAX = 2_147_483_647

class Solution:

    def nextGreaterElement(self, n: int) -> int:
        """   
        starting form the least significatn bit, 
        """
        def int2digits(x):
            result = []
            while x >0:
                x, digit = divmod(x,10)
                result.append(digit)
            return result[::-1]

        def digits2int(digits):
            x = 0
            for dig in digits:
                x *= 10
                x += dig
            return x
            
        
        digits = int2digits(n)

        i = len(digits) -2
        #Fidn pivot
        while i>= 0 and digits[i] >= digits[i+1]:
            i -= 1

        if i < 0:
            return -1

        
        j = len(digits)- 1
        while digits[j] <= digits[i]:
            j -= 1

        digits[i], digits[j] = digits[j], digits[i]


        digits[i+1:] = reversed(digits[i+1:])
        result = digits2int(digits)
        if result > MAX:
            
            return -1
        return result


        
# @lc code=end

