#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        we Count how many numbers have a bit set in each position
        all counts of the repeated numbers should be divisble by the number of repetitions 3 in this case
        """
        REPETITIONS = 3
        bit_count = [0] * 32

        for num in nums:
            x = num & 0xFFFFFFFF
            for i in range(len(bit_count)):
                bit_count[i] += (x >> i) & 1
        print(bit_count)
        #Take it modulo the number of repetitions, to get the bits fo the unique number
        result = 0
        for i in range(len(bit_count)):
            if bit_count[i] % REPETITIONS == 1:
                result |= (1 << i)
        #Convert back to twos complement negative number     
        if result >= 2**31:
            result -= 2**32
        return result
                 
        
        
# @lc code=end

