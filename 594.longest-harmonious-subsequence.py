#
# @lc app=leetcode id=594 lang=python3
#
# [594] Longest Harmonious Subsequence
#

# @lc code=start

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            if not num in counts:
                counts[num] = 0
            counts[num] += 1
        nums.sort()
        max_len = 0
        for key in nums:
            if key in counts and (key+1) in counts:
                max_len = max(max_len, counts[key]+ counts[key+1])
        
        return max_len

            
        
# @lc code=end

