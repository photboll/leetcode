#
# @lc app=leetcode id=2099 lang=python3
#
# [2099] Find Subsequence of Length K With the Largest Sum
#

# @lc code=start

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        """
        This is equivalent to finding the k largest numbers in nums 
        """
        result = [(i, num) for i, num in enumerate(nums)]
        result.sort(reverse=True, key = lambda x: x[1])
        result = result[:k]
        result.sort()
        return [ num for _, num in result]
        
# @lc code=end

