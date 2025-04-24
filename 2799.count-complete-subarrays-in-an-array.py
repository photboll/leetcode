#
# @lc app=leetcode id=2799 lang=python3
#
# [2799] Count Complete Subarrays in an Array
#

# @lc code=start
from collections import Counter
class SolutionBF:
    def countCompleteSubarrays(self, nums):
        count_distinct = len(set(nums))
        n = len(nums)
        result = 0
        for left in range(n):
            for right in range(left+count_distinct, n+1):
                if len(set(nums[left:right])) == count_distinct:
                    result += 1
        return result
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        count_distinct = len(set(nums))
        window_counts = Counter()
        left = 0
        answer = 0
        n = len(nums)
        for right in range(n):
            #add the current number to the window 
            window_counts[nums[right]] += 1
            if len(window_counts) < count_distinct:
                #Keep expanding window till we have atleast every distinct number in it
                continue

            #Here we can assume that we have atleast one of every distinctnumber in the window
            #How many subarrays(starting points left) ending at right will also have be complete?
            #Any superarray of this array will also be complete of which there are n - right
            while len(window_counts) == count_distinct:
                answer += n - right
                window_counts[nums[left]] -= 1
                if window_counts[nums[left]] == 0:
                    del window_counts[nums[left]]
                left += 1
        return answer
            
            

        
        
# @lc code=end

