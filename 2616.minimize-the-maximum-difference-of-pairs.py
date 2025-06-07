#
# @lc app=leetcode id=2616 lang=python3
#
# [2616] Minimize the Maximum Difference of Pairs
#

# @lc code=start
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def can_find_pairs(nums, max_diff, num_pairs):
            pair_count = 0
            i = 0
            while i + 1 < len(nums):
                if abs(nums[i]- nums[i+1]) <= max_diff:
                    pair_count += 1
                    i += 2
                else:
                    i += 1
            return pair_count >= num_pairs
        
        nums.sort()
        low, high= 0, nums[-1] - nums[0]
        while low < high:
            mid = (low + high)// 2

            if can_find_pairs(nums, mid, p):
                high = mid
            else:
                low = mid + 1
        return low 
            
                    
        
# @lc code=end

