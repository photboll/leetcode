#
# @lc app=leetcode id=2654 lang=python3
#
# [2654] Minimum Number of Operations to Make All Array Elements Equal to 1
#

# @lc code=start
from math import gcd
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        as soon as we have a 1 in nums we can transform all non 1s to 1 at a cost of one operation 
        per each num != 1.
        
        It will be impossible if the lowest gcd for any two num is larger than 1
        
        """
        n, one_count, cd = len(nums), 0, 0
        
        for x in nums:
            if x == 1:
                one_count += 1
            cd = gcd(cd, x)


        if one_count > 0:
            return n - one_count
        
        if cd > 1:
            return -1
        
        min_len = n
        for i in range(n):
            cd = 0
            for j in range(i, n):
                cd = gcd(cd, nums[j])
                if cd == 1:
                     min_len = min(min_len, j -i +1)
                     break
                     
        return min_len + n - 2
        
# @lc code=end

