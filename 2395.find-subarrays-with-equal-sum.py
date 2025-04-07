#
# @lc app=leetcode id=2395 lang=python3
#
# [2395] Find Subarrays With Equal Sum
#

# @lc code=start
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        #We add to a dict with keys being the sum and values being the index of the beginning
        sumToi = {}
        n = len(nums)
        for i in range(n-1):
            curSum = nums[i] + nums[i+1]
            if curSum in sumToi:
                return True
            sumToi[curSum] = i
        return False
        
# @lc code=end

