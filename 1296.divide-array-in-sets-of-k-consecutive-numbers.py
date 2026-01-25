#
# @lc app=leetcode id=1296 lang=python3
#
# [1296] Divide Array in Sets of K Consecutive Numbers
#

# @lc code=start
from collections import Counter
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()
        freqs = Counter(nums)

        for num in nums:
            if freqs[num] > 0:
                #print(num, num+k, freqs)
                for i in range(num, num+k):
                    freqs[i] -= 1
                    if freqs[i] < 0:
                        return False
        return True
                    

        
# @lc code=end

