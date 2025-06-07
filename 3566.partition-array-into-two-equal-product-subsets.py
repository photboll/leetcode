#
# @lc app=leetcode id=3566 lang=python3
#
# [3566] Partition Array into Two Equal Product Subsets
#

# @lc code=start
class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        """
        can we simply try all combinations?
        """
        
        def dfs(i, prod1, prod2):
            #print(i, prod1, prod2)
            if i == len(nums) and prod1 == prod2== target:
                return True
            elif prod1 > target or prod2> target or i == len(nums):
                return False

            #we can either include nums[i] or leave it in the other subset
            return dfs(i+1, prod1*nums[i], prod2) or dfs(i+1, prod1, prod2 * nums[i])
        
        return dfs(1, nums[0], 1) or dfs(1, 1, nums[0])

        
# @lc code=end

