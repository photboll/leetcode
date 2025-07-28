#
# @lc app=leetcode id=2044 lang=python3
#
# [2044] Count Number of Maximum Bitwise-OR Subsets
#

# @lc code=start
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        """
        the maximum bitwise OR is easily find by simply ORing all nums
        n <= 16 which is very small, can probably enumerate all combos 
        """
        max_or_bit = 0
        for num in nums:
            max_or_bit |= num

        n = len(nums)
        nums.sort(reverse=True)
        
        subset = []
        result = [0]
        def backtrack(i, curr_or_bit):
            if curr_or_bit == max_or_bit:
                result[0] = result[0] + 1
                
            
            for j in range(i+1, n):
                subset.append(nums[j])
                backtrack(j, curr_or_bit | nums[j])
                subset.pop()
        
        backtrack(-1, 0)
        return result[0]
                
        
        
        
# @lc code=end

