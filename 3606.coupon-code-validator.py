#
# @lc app=leetcode id=3606 lang=python3
#
# [3606] Coupon Code Validator
#

# @lc code=start
SECTORS = {"electronics", "grocery", "pharmacy", "restaurant"}
class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        
        def is_valid(code, businessLine, isActive):
            if not isActive:
                return False
            if businessLine not in SECTORS:
                return False
            if not code.replace("_", "A").isalnum():
                return False
            
            return True
        
        result = []
        for i in range(len(code)):
            line = [code[i], businessLine[i], isActive[i]]
            if is_valid(*line):
                result.append(line)
        
        result.sort(key=lambda x: x[0])
        result.sort(key=lambda x: x[1])

        
        return [line[0] for line in result]
        
# @lc code=end

