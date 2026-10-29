# @lc app=leetcode id=3841 slug=palindromic-path-queries-in-a-tree lang=python3
#
# [3841] Palindromic Path Queries in a Tree
# Difficulty: Hard
# Tags: Array, String, Divide and Conquer, Bit Manipulation, Tree, Depth-First Search, Binary Indexed Tree, Segment Tree
# URL: https://leetcode.com/problems/palindromic-path-queries-in-a-tree/
#
# @lc code=start
class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n+1)
    
    def lowbit(self, x: int):
        return x & -x
    
    def update(self, x, v):
        while x <= self.n:
            self.tree[x] ^= v
            x += self.lowbit(x)
        
    def query(self, x):
        ret = 0

        while x:
            ret ^= self.tree[x]
            x -= self.lowbit(x)
        return ret 
    
    def updateRange(self, l, r, v):
        self.update(l, v)
        self.update(r+1, v)
    

        
class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        g = [[] for _ in range(n)]

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        LOG = n.bit_length()

        fa = [[0] * LOG for _ in range(n)]
        dep = [0] * n
        l = [0] * n
        r = [0] * n
        timer = 0
        
        def dfs(u, p):
            nonlocal timer
            timer += 1

            l[u] = timer
            fa[u][0] = p
            for v in g[u]:
                if v == p:
                    continue

                dep[v] = dep[u] + 1
                dfs(v, u)
            r[u] = timer
        
        dfs(0, 0)

        for j in range(1, LOG):
            for i in range(n):
                fa[i][j] = fa[fa[i][j-1]][j-1]
        
        def lca(u, v):
            if dep[u] < dep[v]:
                u, v = v, u
            diff = dep[u]  - dep[v]
            for i in range(LOG):
                if (diff >> i) & 1:
                    u = fa[u][i]
            if u == v:
                return u
            
            for i in range(LOG-1, -1, -1):
                if fa[u][i] != fa[v][i]:
                    u = fa[u][i]
                    v = fa[v][i]
            return fa[u][0]
        
        
        bit = BinaryIndexedTree(n+1)
        s = list(s)
        for i in range(n):
            bit.updateRange(l[i], r[i], 1 << (ord(s[i]) - ord("a")))
        
        ans = []
        for q in queries:
            op, *rest = q.split()
            if op == "update":
                u, c = int(rest[0]), rest[1]
                bit.updateRange(
                    l[u],
                    r[u],
                    (1 << (ord(s[u]) - ord("a")) ^ (1 << (ord(c) - ord("a"))))
                )

                s[u] = c
            
            else:
                u, v = int(rest[0]), int(rest[1])
                w = lca(u, v)

                mask = (
                    bit.query(l[u])
                    ^ bit.query(l[v])
                    ^ (1 << (ord(s[w]) - ord("a")))
                )
                ans.append(mask.bit_count() <= 1)
        return ans




        

# @lc code=end
