#
# @lc app=leetcode id=1320 lang=python3
#
# [1320] Minimum Distance to Type a Word Using Two Fingers
#

# @lc code=start
class Solution:
    def minimumDistance(self, word: str) -> int:
        """
        l1 distance 
        dp[k][i] = min distance to type 0:k with the other finger positioned at i. the first finger is on word[k]

        """

        def c2idx(c):
            return ord(c) - ord("A")

        def distance(i, j):
            #i, j are the indices of the chars in ascii_uppercase
            return distance_l1(*divmod(i, 6), *divmod(j, 6))

        def distance_l1(x1, y1, x2, y2):
            return abs(x1-x2) + abs(y1-y2)

        dp = [[float("inf")] * 26 for _ in range(len(word))]
        #Base case
        for i in range(26):
            dp[0][i] = 0

        for k in range(len(word) -1):
            cur = c2idx(word[k])
            nxt = c2idx(word[k+1])
            for j in range(26):
                # same finger, the other thinger is left in its own position
                dp[k+1][j] = min(dp[k+1][j],
                                dp[k][j] + distance(cur, nxt))

                # switch finger, other thinger moves to word[k]
                dp[k+1][cur] = min(dp[k+1][cur],
                                    dp[k][j] + distance(j, nxt))
        
        return min(dp[-1])

                    




        
        
# @lc code=end

