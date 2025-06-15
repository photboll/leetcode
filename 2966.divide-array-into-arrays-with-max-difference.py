#
# @lc app=leetcode id=2966 lang=python3
#
# [2966] Divide Array Into Arrays With Max Difference
#

# @lc code=start
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        """
        main idea, sort the numbers and simply divide them into subarrays of length 3
        """
        result = []
        nums.sort()

        for i in range(0, len(nums), 3):
            if nums[i+2] - nums[i] > k:
                return []
            else:
                result.append(nums[i:i+3])
        return result
            
        
# @lc code=end

