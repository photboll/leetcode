#
# @lc app=leetcode id=462 lang=python3
#
# [462] Minimum Moves to Equal Array Elements II
#

# @lc code=start
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        """
        We are not actually asked to provide the resulting array itself
        we can find the weighted mean
        1, 10, 2, 9
        at level 1: 0+9+1+8 = 18
        at level 2: 1+8+0+7 = 16
        at level 3: 2+7+1+6 = 16
        at level 4: 3+6+2+5 = 16
        at level 5: 4+5+3+4 = 16
        
        this example was symmetric around the median so we have multiple possible target levels
        No different approach.
        we pair each largest and smallest number with each (a, b)
        regardless of which level they would meet at 
        we need to do a total of abs(b-a) operation in total on the pair.
        provided that the meeting point is between them 
        """

        nums.sort()
        n = len(nums)
        mid = n // 2
        median = nums[mid]
        
        result = 0
        for num in nums:
            result += abs(num - median)

        return result 
        
# @lc code=end

