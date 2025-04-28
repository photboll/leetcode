#
# @lc app=leetcode id=2302 lang=python3
#
# [2302] Count Subarrays With Score Less Than K
#

# @lc code=start

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """
        all nums are larger than 1, implies any superarry must have score strictly larger than the subarray
        So any subarray of an array that have a score of less than k will also have score less than k.
        Will it be useful to precomupte the products of some subarrays? i don't thikn it is necessary
        or is a sliding window approach sufficient?
        We want to find the largest subarray that ends at index right, that have a score less than k.
        We should always shirnk the window from the left side, increment i 
        
        """

        n = len(nums)
        curr_sum = 0
        left = 0
        result = 0
        for right in range(n):
            curr_sum += nums[right]
            curr_score = curr_sum * (right - left + 1) # +1 since the both boundaries are inclusive 
            
            #at this point the window will have ascore that is slightly too large
            #So we need to shrink the window until we are within k again
            while curr_score >= k:
                curr_sum -= nums[left]
                left += 1
                curr_score = curr_sum * (right -left +1)
            
            #at this point, the window is as large as possible with a score less than k
            #The window and all of its possible subarrays will have a score stritly less than k
            #add the triangle numbe of the current window size to the count 
            result += right-left + 1
            #print(nums[left:right+1], left, right, result, curr_sum, curr_score)
            

        return result 
# @lc code=end

