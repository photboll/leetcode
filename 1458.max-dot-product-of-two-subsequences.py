#
# @lc app=leetcode id=1458 lang=python3
#
# [1458] Max Dot Product of Two Subsequences
#

# @lc code=start
from functools import cache
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        """  Dp longest common subsequence-esque 
        dp[i][j] is the maximum dot porduct of two subsequences starting at
        nums1[i:] and nums2[j:]

        4 choices:
        1. extend the subsequnce with the two currently considered elements. continue on i++, j++
        2. skip both
        3. skip the current element in nums1
        4. skip the current element in nums2
        
        """

        
        @cache
        def dp(i, j):
            if i >= len(nums1) or j >= len(nums2):
                #invalid state return 
                return float("-inf")

            curr = nums1[i] * nums2[j]
            return max(
                curr + dp(i+1, j+1), #we add the current product to the max subsequnce
                curr,  # end the sequence here
                dp(i+1, j),# skip candidate in nums1 
                dp(i, j+1)
            )

            
        return dp(0, 0)
        
        
        
# @lc code=end

