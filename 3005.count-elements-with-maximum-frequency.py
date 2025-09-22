#
# @lc app=leetcode id=3005 lang=python3
#
# [3005] Count Elements With Maximum Frequency
#

# @lc code=start
from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqs = Counter(nums)
        most_common = freqs.most_common()
        _, max_freq= most_common[0]
        total = 0
        for _, freq in most_common:
            if freq == max_freq:
                total += freq
            else:
                break 
        return total 

        
# @lc code=end

