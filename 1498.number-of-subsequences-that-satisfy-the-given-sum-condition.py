#
# @lc app=leetcode id=1498 lang=python3
#
# [1498] Number of Subsequences That Satisfy the Given Sum Condition
#

# @lc code=start

MAX_N = 100000
MOD = pow(10, 9) + 7
POWERS_2 = [1] * MAX_N
POWERS_2[0] = 1
for i in range(1, MAX_N):
    POWERS_2[i] = (POWERS_2[i-1] *2) % MOD
    
 
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        """
        Sort and use two pointers to count all possible subsequnces
        n can be very large 10**5 need to be smart about computing all possible non/empty seqs
        """
        

        n = len(nums)
        nums.sort()
        count = 0
        
        l = 0
        r = n-1
        while l <= r:
            if nums[l] + nums[r] <= target:
                count = (count + POWERS_2[r - l]) % MOD
                l += 1
            else:
                r -= 1   
       
        return count 
        
# @lc code=end

