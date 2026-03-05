#
# @lc app=leetcode id=1758 lang=python3
#
# [1758] Minimum Changes To Make Alternating Binary String
#

# @lc code=start
class Solution:
    def minOperations(self, s: str) -> int:
        def ops_to_target(s, target):
            ops = 0
            for i in range(len(s)):
                if s[i] != target:
                    ops += 1
                
                if target == "1":
                    target = "0"
                else: 
                    target = "1"
            return ops

        #Pattern 1 0x555555.. 101010...
        # Pattern 2 0xAAAAAAA... 0101010....

        return min(ops_to_target(s, "1"), ops_to_target(s, "0"))

        
# @lc code=end

