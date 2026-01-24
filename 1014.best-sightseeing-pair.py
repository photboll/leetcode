#
# @lc app=leetcode id=1014 lang=python3
#
# [1014] Best Sightseeing Pair
#

# @lc code=start
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        """
        values[i] + values[j] + i - j = values[i] + i + (values[j] - j)
        the term values[j] - j is only dependent on j
        so we can always compare the current position with the position which have the laregst values[j] - j
        """
        n = len(values)
        best_start_score = values[0]
        result = -1

        for i in range(1, n):
            curr_score = values[i] - i
            result = max(curr_score + best_start_score, result)
            best_start_score = max(values[i] + i, best_start_score)

        
        return result
            
            
        
# @lc code=end

