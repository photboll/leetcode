#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        right_freqs = Counter(s)
        left_freqs = Counter()
        start = -1
        result = []
        for i, char in enumerate(s):
            left_freqs[char] += 1
            right_freqs[char] -= 1
            
            if right_freqs[char] == 0:
                valid_split = True
                for key in left_freqs:
                    if right_freqs[key] != 0:
                        valid_split = False
                        break
                if valid_split:
                    left_freqs.clear()
                    result.append(i - start)
                    start = i
        return result
        
# @lc code=end

