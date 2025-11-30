#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#

# @lc code=start
from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cur_sum = 0
        #map to hold the possible starting positions 
        poss_start = defaultdict(list)
        poss_start[0].append(-1)# to get subarrays starting from the first position
        count = 0
        for i, num in enumerate(nums):
            cur_sum = (cur_sum + num + k) % k# extra + k inorder to always have the positive remainder 

            # a subarrray that is divisible by K and ends at i that is
            count += len(poss_start[cur_sum])
            #for start in poss_start[cur_sum]:
                #print(nums[start+1:i+1])

            poss_start[cur_sum].append(i)
        
        return count 




        
# @lc code=end

