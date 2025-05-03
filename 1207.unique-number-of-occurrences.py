#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#

# @lc code=start
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter()
        for num in arr:
            counts[num] += 1
        
        seen = set()
        for key in counts:
            if counts[key] in seen:
                return False
            seen.add(counts[key])

        return True
        
# @lc code=end

