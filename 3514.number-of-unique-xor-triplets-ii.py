#
# @lc app=leetcode id=3514 lang=python3
#
# [3514] Number of Unique XOR Triplets II
#

# @lc code=start
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        ones = set()
        twos = set()

        for x in nums:
            ones.add(x)
            for y in ones:
                twos.add(x ^ y)
        
        threes = set()
        for z in nums:
            for num in twos:
                threes.add(z ^ num)


        return len(threes)
            
                

        
# @lc code=end

