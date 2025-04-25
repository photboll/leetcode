#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        window_sum = 0
        for i in range(k):
            window_sum += nums[i]
        print(window_sum)
        max_avg = window_sum / k
        for start in range(0, n-k):
            #Let the last element exit the window 
            window_sum -= nums[start]
            window_sum += nums[start+k]
            #print(nums[start+1:start+k+1], window_sum/k)
            max_avg = max(max_avg, window_sum/k)
        return max_avg
            
        
# @lc code=end

