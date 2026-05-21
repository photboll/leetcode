#
# @lc app=leetcode id=1674 lang=python3
#
# [1674] Minimum Moves to Make Array Complementary
#

# @lc code=start
class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        """
        what is the optimal target sum?
        the mode of the sums? 
        but, is it pos>sible for a pair to be out of reach for the mode?
        2 * limit is the maximum we can reach with replacements 
        
        
        every pair needs either 0, 1 or 2 modifications to reach the target sum

        0 if a + b == target

        
        
        
        """

        n = len(nums)

        #if we change any pair then the result must be in [2, 2*limit]
        diff = [0] * (2*limit + 2)

        for i in range(n//2):
            a = nums[i] 
            b = nums[n-1-i]

            low = min(a,b) + 1
            high = max(a, b) + limit

            #2 modifications everywhere
            diff[2] += 2

            #1 modification from low to high+1
            diff[low] -= 1
            diff[high+1] += 1

            #0 modiciations on s
            s = a + b
            diff[s] -= 1
            diff[s + 1] +=1
        
        
        res = float("inf")

        curr = 0

        for target in range(2, 2*limit+1):
            curr += diff[target]
            res = min(res, curr)
        return res
            
        
        




        
        
# @lc code=end

