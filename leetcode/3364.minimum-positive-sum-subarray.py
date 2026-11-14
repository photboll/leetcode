# @lc app=leetcode id=3364 slug=minimum-positive-sum-subarray lang=python3
#
# [3364] Minimum Positive Sum Subarray 
# Difficulty: Easy
# Tags: Array, Sliding Window, Prefix Sum
# URL: https://leetcode.com/problems/minimum-positive-sum-subarray/
#
# @lc code=start

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        
        prefix_s = [0] * (n+1)
        result = float("inf")
        #print(nums)
        for i in range(n):
            prefix_s[i+1] = prefix_s[i] + nums[i]

        for i in range(1, n+1):
            for k in range(l, r+1):
                if i-k <0:
                    break
                
                cur_window = prefix_s[i] - prefix_s[i-k]
                #print(i-k, i, cur_window)

                if 0 < cur_window < result:
                    result = cur_window


        return result if 0 < result < float("inf") else -1
                
        
        

        
        

# @lc code=end
