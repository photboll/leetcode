#
# @lc app=leetcode id=2918 lang=python3
#
# [2918] Minimum Equal Sum of Two Arrays After Replacing Zeros
#

# @lc code=start
def nums_to_sum_interval(nums):
    zeros = 0
    tot = 0
    for num in nums:
        if num == 0:
            zeros += 1
        else:
            tot += num
    return tot + zeros, zeros == 0 
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Must replace all 0s.
        When is it impossible?
        is it always possible if both array scontains at least one zero?
        If an array does not contain any zero, then its sum is fixed 
        If an array contains atelast a zero then we can make its sum equal any number that is ge tot1 + zeros1 
        Then we can find the smallest number that overlaps thse two intervals 
        """
        min1, sum_is_fixed1 = nums_to_sum_interval(nums1)
        min2, sum_is_fixed2 = nums_to_sum_interval(nums2)
        #print(min1, sum_is_fixed1, min2, sum_is_fixed2)
        
        if sum_is_fixed1 and sum_is_fixed2:
            return min1 if min1 == min2 else -1
        elif sum_is_fixed1:
            return min1 if min2 <= min1 else -1
        elif sum_is_fixed2:
            return min2 if min1 <= min2 else -1
        else:
            #Both arrays can take on any value larger than their current sum 
            return max(min1, min2)


        
# @lc code=end

