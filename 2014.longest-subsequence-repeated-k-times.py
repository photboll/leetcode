#
# @lc app=leetcode id=2014 lang=python3
#
# [2014] Longest Subsequence Repeated k Times
#

# @lc code=start
from collections import Counter, deque
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        """
        Chars with frequencey less then k, cant possibly be part of such a subsequenvce
        """
        answer = ""
        candidate_chars = sorted(
            [c for c, w in Counter(s).items() if w >= k], reverse=True
        )
        q = deque(candidate_chars)
        while q:
            curr = q.popleft()
            if len(curr) > len(answer):
                answer = curr
            
            for ch in candidate_chars:
                next = curr + ch
                it = iter(s)
                if all(ch in it for ch in next * k):
                    q.append(next)
        return answer
                
        
        
        
# @lc code=end

