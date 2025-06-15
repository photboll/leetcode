#
# @lc app=leetcode id=1432 lang=python3
#
# [1432] Max Difference You Can Get From Changing an Integer
#

# @lc code=start
class Solution:
    def maxDiff(self, num: int) -> int:
        """
        Take the first none-nine digit and change it to 9, that gives the maximum
        To get the minimum: if the first digit is larger than 1, we can replace it with 1 to get the minimum 
        if the first digit is 1. then we need to find the first non-1 or non-0 digit and change it to zero 
        """

        def remap(digits, src, trg):
            for i in range(len(digits)):
                if digits[i] == src:
                    digits[i] = trg
            return digits

        def remap_max(num):
            digits = [c for c in str(num)]
            for i in range(len(digits)):
                if digits[i] != "9":
                    remap(digits, digits[i], "9")
                    break
            return int("".join(digits))
        
        def remap_min(num):
            digits = [c for c in str(num)]

            if digits[0] > "1":
                remap(digits, digits[0], "1")
                return int("".join(digits))
                
            for i in range(1, len(digits)):
                if digits[i] > "1":
                    remap(digits, digits[i], "0")
                    break
            
            return int("".join(digits))
        a = remap_max(num)    
        b = remap_min(num)
        #print(a, b)

        return a - b
            
# @lc code=end

