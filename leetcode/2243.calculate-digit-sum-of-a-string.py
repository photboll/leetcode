# @lc app=leetcode id=2243 slug=calculate-digit-sum-of-a-string lang=python3
#
# [2243] Calculate Digit Sum of a String
# Difficulty: Easy
# Tags: String, Simulation
# URL: https://leetcode.com/problems/calculate-digit-sum-of-a-string/
#
# @lc code=start
class Solution:
    def digitSum(self, s: str, k: int) -> str:

        
        def digSum(x:int ):
            s = 0
            while x > 0:
                x, digit = divmod(x, 10)
                s += digit 
            return s
        
        
        while len(s) > k:
            new_s = []
            for i in range(0, len(s), k):
                new_s.append(str(digSum(int(s[i:min(i+k, len(s))]))))
            
            s = "".join(new_s)
                
        return s 
            


        

# @lc code=end
