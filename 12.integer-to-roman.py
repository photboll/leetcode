#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start

sym2i = {"I": 1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000,
        "IV": 4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
i2sym = {v : k for k, v in sym2i.items()}
class Solution:
    def intToRoman(self, num: int) -> str:
        result = []
        digit_pos = 1 #We start with the least significant digit 
        while num > 0:
            num, cur_digit = divmod(num, 10)
            if cur_digit < 4:
                roman = cur_digit * i2sym[digit_pos]
            elif cur_digit == 4 or cur_digit == 9:
                #Use subtractive form
                roman = i2sym[cur_digit*digit_pos]
            elif cur_digit == 5:
                roman = i2sym[5*digit_pos] #Add the V L or D once
            else:
                #Else 6, 7,8 
                roman = i2sym[5*digit_pos] #Add the V L or D once
                rem = cur_digit - 5
                roman += rem * i2sym[digit_pos]
                
            result.append(roman)  
            
            digit_pos *= 10
        return "".join(result[::-1])
        
# @lc code=end

