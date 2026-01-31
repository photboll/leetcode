#
# @lc app=leetcode id=2977 lang=python3
#
# [2977] Minimum Cost to Convert String II
#

# @lc code=start
INF = 1 << 63
MAX_ADJ_LIST = 201

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        s2i = {}
        lengths = set()
        size = 0

        #Floyw Warshall to create adjecency list
        dist = [[INF]*MAX_ADJ_LIST for _ in range(MAX_ADJ_LIST)]
        for s, t, w in zip(original, changed, cost):
            if s not in s2i:
                s2i[s] = size
                lengths.add(len(s))
                size += 1
            if t not in s2i:
                s2i[t] = size
                size += 1
            
            si = s2i[s]
            dist[si][si] = 0
            ti = s2i[t]
            dist[si][ti] = min(dist[si][ti], w)
        
        for k in range(size):
            for i in range(size):
                if dist[i][k] >= INF:
                    continue
                for j in range(size):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        
        #dp 
        n = len(source)
        dp = [INF] * (n+1)
        dp[0] = 0

        for i in range(n):
            if dp[i] == INF:
                continue
            
            if source[i] == target[i]:
                dp[i+1] = min(dp[i+1], dp[i])
            
            for l in lengths:
                if i + l > n:
                    continue
                s = source[i:i+l]
                t = target[i:i+l]
                if s in s2i and t in s2i:
                    dp[i+l] = min(dp[i+l]
                                  , dp[i] + dist[s2i[s]][s2i[t]]
                                  )
        return -1 if dp[n] == INF else dp[n]

        
        
        
        

            
            

        
        
# @lc code=end
