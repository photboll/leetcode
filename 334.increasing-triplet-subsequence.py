#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#

# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        Lets consider the middle indexe j, 
        1. it nedds to have a number to the left of it that is smaller than nums[j]
        2. it nees to have a number to the right of it that is larger than nums[j]
        if we conside each j in range(0,n), at each step each number gets moved from the right larger than pile
        to the left smaller than pile.
        for the left side we cna simply keep track of min value seens so far and compare it to nums[j]
        can we simply to do it in two passes, one forawrd and one backward, 
        if we 
        """
        first = float("inf") 
        second = float("inf") 
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False
# @lc code=end

