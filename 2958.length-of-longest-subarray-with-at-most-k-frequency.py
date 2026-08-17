#
# @lc app=leetcode id=2958 lang=python3
#
# [2958] Length of Longest Subarray With at Most K Frequency
#

# @lc code=start
from collections import defaultdict, Counter
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        """
        sliding window and we always make sure that the window is good 
        """
        n = len(nums)
        freqs = Counter()
        l = 0
        result = 0

        for r in range(n):
            num = nums[r]
            freqs[num] += 1
            #shrink window if we exceed k. i.e. window is no longer good
            while freqs[num] > k:
                #it is safe to ignore bounds checking l and the count of freqs. since k>=1 when l == r freqs[] = 0 for all nums
                freqs[nums[l]] -= 1
                l += 1
            
            result = max(
                result, 
                r - l + 1#current size of window
                         )
        return result 
            

            
        
        
# @lc code=end

