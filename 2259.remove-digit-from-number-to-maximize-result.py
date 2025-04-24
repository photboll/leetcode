#
# @lc app=leetcode id=2259 lang=python3
#
# [2259] Remove Digit From Number to Maximize Result
#

# @lc code=start
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        #can we check what the value will be for each possible location?
        #is that efficient enough
        maxNum= 0
        for i, char in enumerate(number):
            if char == digit:
                #what do we get if we remove this one 
                new_num = int(number[:i] + number[i+1:])
                #print(new_num)
                maxNum = max(new_num, maxNum)
        
        return str(maxNum)
                
        
# @lc code=end

