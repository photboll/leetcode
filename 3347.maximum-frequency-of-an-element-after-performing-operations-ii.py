#
# @lc app=leetcode id=3347 lang=python3
#
# [3347] Maximum Frequency of an Element After Performing Operations II
#

# @lc code=start
from collections import defaultdict
from sortedcontainers import SortedSet
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        """
        sliding window
        any potential number could be target to be the one with maximum frequency
        We can always use +0 on any number if we dont need more numOperations,
        
        any number in [target-k,targe+k] can be transformed to target 
        """
        freq = defaultdict(int)
        sweep = defaultdict(int)
        target_candidates = SortedSet()
        for x in nums:
            freq[x] +=1
            s = x -k
            t=  x+k+1
            sweep[s] += 1
            sweep[t] -= 1
            target_candidates.add(x)
            target_candidates.add(s)
            target_candidates.add(t)
        
        res = 0
        count = 0
        for x in target_candidates:
            count += sweep[x]
            res = max(res, min(count, freq[x] + numOperations))
        return res
            
        
# @lc code=end

