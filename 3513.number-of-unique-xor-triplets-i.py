#
# @lc app=leetcode id=3513 lang=python3
#
# [3513] Number of Unique XOR Triplets I
#

# @lc code=start
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        n = max(nums)

        max_set_bit = n.bit_length()

        return (1 << (max_set_bit ) )

        
# @lc code=end

