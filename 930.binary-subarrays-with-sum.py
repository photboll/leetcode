#
# @lc app=leetcode id=930 lang=python3
#
# [930] Binary Subarrays With Sum
#

# @lc code=start
from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        
        prefix_sum = 0
        freq = defaultdict(int)
        freq[0] = 1
        for num in nums:
            prefix_sum += num
            count += freq[prefix_sum - goal]
            freq[prefix_sum] += 1
        return count
        
# @lc code=end

