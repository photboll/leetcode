#
# @lc app=leetcode id=659 lang=python3
#
# [659] Split Array into Consecutive Subsequences
#

# @lc code=start
from collections import Counter
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        """  
        is there any reason not to be greedy here? yes if example 1 is attempted greedily 
        """
        freqs = Counter(nums)
        end = {}
        
        for num in nums:
            if freqs[num] == 0:
                continue

            #can we extend one of our current sequences
            if end.get(num-1, 0) > 0:
                end[num-1] -= 1
                end[num] = end.get(num, 0) + 1
                freqs[num] -= 1
            #can we start a new sequence from num
            elif freqs.get(num+1, 0) > 0 and freqs.get(num+2, 0) > 0:
                freqs[num] -= 1
                freqs[num+1] -= 1
                freqs[num+2] -= 1
                end[num+2] = end.get(num+2, 0) + 1
            else:
                return False

        return True

# @lc code=end

