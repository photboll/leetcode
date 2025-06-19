#
# @lc app=leetcode id=2138 lang=python3
#
# [2138] Divide a String Into Groups of Size k
#

# @lc code=start
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        num_parts = k - n % k
        s += fill * num_parts
        result = []
        for i in range(0, n, k):
            result.append(s[i:i+k])
        return result
        
        
# @lc code=end

