#
# @lc app=leetcode id=2900 lang=python3
#
# [2900] Longest Unequal Adjacent Groups Subsequence I
#

# @lc code=start
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        """
        The first elemetn of words can always be included in the longest alternating sequence
        """

        result = [words[0]]
        prev = groups[0]
        n = len(words)
        for i in range(n):
            if groups[i] != prev:
                result.append(words[i])
                prev =  groups[i]
        return result
            
        
# @lc code=end

