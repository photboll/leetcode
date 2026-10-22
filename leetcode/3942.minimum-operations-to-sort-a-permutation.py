# @lc app=leetcode id=3942 slug=minimum-operations-to-sort-a-permutation lang=python3
#
# [3942] Minimum Operations to Sort a Permutation
# Difficulty: Medium
# Tags: Array
# URL: https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/
#
# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0
        
        #its a permutation of range(n). so either 0 or have to be first or last in the end array
        start = nums.index(0)
        asc = True
        desc = True
        
        #walk nums starting from 0 the next number should always be +1
        i = 1
        while i < n and (asc or desc):
            val = nums[(start + i) % n]

            if val != i:
                asc = False
            if val != n - i:
                desc = False
            
            i += 1
        
        if asc:
            return min(start, n - start + 2)
        elif desc:
            return min(n- start, start + 2)
        else:
            return -1
        
            
            






        

# @lc code=end
