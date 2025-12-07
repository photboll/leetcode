#
# @lc app=leetcode id=2035 lang=python3
#
# [2035] Partition Array Into Two Arrays to Minimize Sum Difference
#

# @lc code=start
from collections import defaultdict
from bisect import bisect_left
from itertools import combinations

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        """
        We want the two subarrays to have sum as close as poosible to each other
        
        sum(nums) / 2 is the target 
        
        """
        def subset_sums(arr):
            #sum_arr will hold the set of all possible sums when selecting k elements from arr
            sum_arr = defaultdict(list)
            n = len(arr)
            for k in range(n+1):
                sums = set()
                for combo in combinations(arr, k):
                    sums.add(sum(combo))
                sum_arr[k] = sorted(list(sums))
            return sum_arr
        n = len(nums)
        mid = n // 2
        l1 = subset_sums(nums[:mid])
        l2 = subset_sums(nums[mid:])
        target = sum(nums) / 2
        result = float("inf")
        for k1 in range(mid+1):
            #we select k1 elements from subset l1 and mid - k1 elements from subset l2 
            #These two subsets will then form one of the partitions 
            k2 = mid - k1
            #print(target, k1, k2, l1[k1], l2[k2])
            for s1 in l1[k1]:
                #s1 + s2 should be as close to target as possible
                #find sums in l2 that are close to target - s1
                closest_i = bisect_left(l2[k2], target - s1)
                n2 = len(l2[k2])
            
                #i - 1, i and i+1 are the only candidate solutions
                #
                if closest_i < n2:# i
                    result = min(result, abs(s1 + l2[k2][closest_i] - target))
                if closest_i > 0: # i -1 
                    result = min(result, abs(s1 + l2[k2][closest_i-1] - target))
                if closest_i < n2 - 1:# i+1 
                    result = min(result, abs(s1 + l2[k2][closest_i+1] - target))
        #print(target, result)
        return int(result * 2)
                
                
# @lc code=end

