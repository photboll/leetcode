#
# @lc app=leetcode id=3714 lang=python3
#
# [3714] Longest Balanced Substring II
#

# @lc code=start
from collections import defaultdict
def longest_one_char_run(s):
    res = 1
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            count = 1
        res = max(res, count)
    return res

WORD_SIZE = 3
class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        prefix = [[0] * WORD_SIZE for _ in range(n+1)]

        for i in range(n):
            for j in range(WORD_SIZE):
                prefix[i+1][j] = prefix[i][j]
            cur = ord(s[i])-97
            prefix[i+1][cur] += 1
        #print(prefix)

        #maps signature to the earliest index of when we saw it 
        sig2first = {}
        res = 0

        for i, (a, b, c) in enumerate(prefix):
            for case in [
                (1, a- b, a-c), #a, b, c
                (2, a-b, c),    #a, b
                (3, b-c, a),    #b, c
                (4, c-a, b),    #a, c
                (5, b, c),      #a
                (6, c, a),      #b
                (7, a, b),      #c
            ]:
                if case not in sig2first:
                    sig2first[case] = i
                else:
                    res = max(res, i - sig2first[case])
        return res
            

        

        

                
        
# @lc code=end

