#
# @lc app=leetcode id=3471 lang=python3
#
# [3471] Find the Largest Almost Missing Integer
#

# @lc code=start
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        """
        
        """
        n = len(nums)
        if k == n:
            return max(nums)

        count = [0] * 51# 0 <= nums[i] <= 50
        for num in nums:
            count[num] += 1
        
        candidates = []
        if k == 1:
            candidates.extend([num for num in nums if count[num] == 1])
        #for any other k only the endpoints will occur exactly once
        else:
            if count[nums[0]] == 1:
                candidates.append(nums[0])
            if count[nums[n-1]] == 1:
                candidates.append(nums[n-1])
        
        if candidates:
            return max(candidates)
        else:
            return -1
    
            

        
        
# @lc code=end

