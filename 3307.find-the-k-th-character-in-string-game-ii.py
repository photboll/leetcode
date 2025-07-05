#
# @lc app=leetcode id=3307 lang=python3
#
# [3307] Find the K-th Character in String Game II
#

# @lc code=start
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        res = 0
        while k != 1:
            t = k.bit_length() - 1
            if (1 << t) == k:
                t -= 1
            k -= 1 << t
            if operations[t]:
                res += 1
                
        return chr(ord("a") + (res % 26))
        
# @lc code=end

