#
# @lc app=leetcode id=3346 lang=python3
#
# [3346] Maximum Frequency of an Element After Performing Operations I
#

# @lc code=start
from bisect import bisect_left, bisect_right
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        """
        sliding window
        any potential number could be target to be the one with maximum frequency
        We can always use +0 on any number if we dont need more numOperations,
        
        any number in [target-k,targe+k] can be transformed to target 
        """
        M = max(nums) + 2
        freq = [0] * M
        sweep = [0] * M
        
        mm = M
        for x in nums:
            freq[x] +=1
            s, t= max(1, x-k), min(M-1, x+k+1)
            sweep[s] += 1
            sweep[t] -= 1
            mm= min(mm, s)
        
        res = 0
        count = 0
        for x in range(mm, M):
            count += sweep[x]
            res = max(res, freq[x] + min(numOperations, count-freq[x]))
        return res
            
            
            
            
            

            


        
# @lc code=end

