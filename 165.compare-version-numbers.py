#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        n = len(v1)
        m = len(v2)

        if n < m:
            v1.extend("0" for _ in range(m-n))
        elif n > m:
            v2.extend("0" for _ in range(n-m))
        
        for chars1, chars2 in zip(v1, v2):
            num1 = int(chars1)
            num2 = int(chars2)

            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
            
        return 0
            

        
# @lc code=end

