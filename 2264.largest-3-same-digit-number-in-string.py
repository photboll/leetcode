#
# @lc app=leetcode id=2264 lang=python3
#
# [2264] Largest 3-Same-Digit Number in String
#

# @lc code=start
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good_ints = set()
        
        for i in range(2, len(num)):
            if num[i-2] == num[i-1] == num[i]:
                good_ints.add(num[i-2:i+1])
        
        if len(good_ints) > 0:
            return max(good_ints)
        return ""

            
        
# @lc code=end

