#
# @lc app=leetcode id=421 lang=python3
#
# [421] Maximum XOR of Two Numbers in an Array
#

# @lc code=start
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        """
        O(N * max_bit_length) Time and O(N) memory
        """
        max_xor = 0
        mask = 0
        for i in range(max(nums).bit_length() - 1, -1, -1):
            mask |= (1 << i)
            prefixes = {num & mask for num in nums}
            greedy = max_xor | (1 << i)
            found = False
            for prefix in prefixes:
                if (greedy ^ prefix) in prefixes:
                    found = True
                    break
            if found:
                max_xor = greedy
        return max_xor

            
        
class SolutionNaive:

    #Time limit exceeded on testcase 33/45
    def findMaximumXOR(self, nums: List[int]) -> int:
        n = len(nums)
        xor_max = 0
        for i in range(n):
            for j in range(i, n):
                xor_max = max(xor_max, nums[i] ^ nums[j])
        
        return xor_max
                
        
# @lc code=end

