#
# @lc app=leetcode id=992 lang=python3
#
# [992] Subarrays with K Different Integers
#

# @lc code=start
from collections import defaultdict, deque
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        """
        sliding window. keep track of how many uniqie elemetns are in the window
        we will want to keep of track of the index were we last saw a specific number
        It might actually be overkill to keep track fo the last seen index. 

        when we have less than k: expand window
        
        more than k: shrink window we l

        """

        freqs = defaultdict(int)
        prev_i = {}
        n = len(nums)
        l = 0
        count = 0
        for r in range(n):
            freqs[nums[r]] += 1
            prev_i[nums[r]] = r

            if len(freqs) < k:
                continue
            
            while len(freqs) > k:
                freqs[nums[l]] -= 1
                if freqs[nums[l]] <= 0:
                    del freqs[nums[l]]
                l += 1
            
            #How do i find the point which would cause us to dip below k elements again? i cal it i
            i = min(prev_i[key] for key in freqs)
            #for j in range(l, i+1):
                #print(nums[j:r+1])
                
            count += i - l + 1
            


        return count
            
        
# @lc code=end

