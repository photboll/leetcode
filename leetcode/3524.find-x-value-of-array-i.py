# @lc app=leetcode id=3524 slug=find-x-value-of-array-i lang=python3
#
# [3524] Find X Value of Array I
# Difficulty: Medium
# Tags: Array, Math, Dynamic Programming
# URL: https://leetcode.com/problems/find-x-value-of-array-i/
#
# @lc code=start
class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        """
        is this not equivialent to finding the number of subarrays in nums. where its product have a remainder of x dviced by k?
        
        """
        n = len(nums)
        result = [0] * k
        dp = [0] * k

        for i in range(n):
            new_dp = [0] * k

            new_dp[nums[i] % k] += 1# the subarray [nums[i]]


            for rem in range(k):
                new_dp[(rem * nums[i]) % k] += dp[rem]

                
            
            dp = new_dp

            for rem in range(k):
                result[rem] += dp[rem]

        return result 

                





        
        

# @lc code=end
