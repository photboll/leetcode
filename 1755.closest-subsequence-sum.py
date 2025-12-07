#
# @lc app=leetcode id=1755 lang=python3
#
# [1755] Closest Subsequence Sum
#

# @lc code=start
from bisect import bisect_left
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        def unique_subseq_sums(arr):
            sums = {0}
            for x in arr:
                sums |= {x + s for s in sums}
            return sums

        n = len(nums)
        mid = n // 2
        
        l1 = sorted(list(unique_subseq_sums(nums[:mid])))
        l2 = sorted(list(unique_subseq_sums(nums[mid:])))
        #print(l1)
        #print(l2)

        #pick one from l1 and one from l2 that minimzes abs(s1 + s2 -goal)

        result = (1 << 64) 
        n2 = len(l2)
        for s1 in l1:
            #binary search for s1 - goal
            closest_i = bisect_left(l2, goal - s1) 
            
            if closest_i < n2:
                result = min(result, abs(s1 + l2[closest_i] - goal))
            if closest_i > 0:
                #the num to the left of closest_i can be added to s1
                result = min(result, abs(s1 + l2[closest_i-1] - goal))
            if closest_i < n2 - 1:
                #the num to tthe right of closest_i can be added to s1
                result = min(result, abs(s1 + l2[closest_i+1] - goal))
            
            #if we find an exact match we can exit early
            if result == 0:
                return result
        return result

            

                
            
        
# @lc code=end

