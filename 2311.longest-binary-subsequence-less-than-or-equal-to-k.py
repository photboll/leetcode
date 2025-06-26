#
# @lc app=leetcode id=2311 lang=python3
#
# [2311] Longest Binary Subsequence Less Than or Equal to K
#

# @lc code=start
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        cur_sum = 0
        cur_len = 0
        bits = k.bit_length()
        for i, char in enumerate(s[::-1]):
            if char == "1":
                if i < bits and cur_sum + (1 << i) <= k:
                    cur_len += 1
                    cur_sum += (1 << i)
            else:
                cur_len
                += 1
        return cur_len
        
# @lc code=end

