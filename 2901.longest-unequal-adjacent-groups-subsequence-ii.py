#
# @lc app=leetcode id=2901 lang=python3
#
# [2901] Longest Unequal Adjacent Groups Subsequence II
#

# @lc code=start
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        """
        dp, each subproblem considers every subsequence ending at position i 
        """

        def hamming_dist_is_k(s1, s2, k=1) -> int:
            if len(s1) != len(s2):
                return False
            
            diff = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff += 1
                    if diff > k:
                        return False
            return diff == k

        n = len(words)
        dp = [1] * n #We can always chose a lone element as an anwser
        prev = [-1] * n # -1 means that there is no previous 
        max_index = 0
        
        
        for i in range(1, n):
            for j in range(i):
                if (
                    (hamming_dist_is_k(words[i], words[j], k=1) )
                    and (dp[j] + 1 > dp[i])
                    and groups[i] != groups[j]
                    ):
                    dp[i] = dp[j] + 1
                    prev[i] = j
                if dp[i] >dp[max_index]:
                    max_index = i
        
        result = []
        i = max_index
        while i >= 0:
            result.append(words[i])
            i = prev[i]

        return result[::-1]
                
        
# @lc code=end

