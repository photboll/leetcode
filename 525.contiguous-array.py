#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#

# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """

        """
        
        s = 0
        max_len = 0
        prev_i = {0:0}

        for i, num in enumerate(nums):
            if num:
                s += 1
            else:
                s -= 1
            
            if s in prev_i:
                max_len = max(max_len, i+1 - prev_i[s])
            else:
                prev_i[s] = i+1
        return max_len

            
        


        
# @lc code=end

