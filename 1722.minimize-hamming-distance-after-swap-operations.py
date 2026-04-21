#
# @lc app=leetcode id=1722 lang=python3
#
# [1722] Minimize Hamming Distance After Swap Operations
#

# @lc code=start
from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.arr = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.arr[x] != x:
            self.arr[x] = self.find(self.arr[x])
        return self.arr[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return 
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.arr[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        """
        allowedswaps edges in a graph 
        
        """
        n = len(source)
        uf = UnionFind(n)
        for u, v in allowedSwaps:
            uf.union(u, v)
        
        sets = defaultdict(lambda : defaultdict(int))
        for i in range(n):
            f = uf.find(i)
            sets[f][source[i]] += 1
        
        result = 0
        for i in range(n):
            f = uf.find(i)
            if sets[f][target[i]] > 0:
                sets[f][target[i]] -= 1
            else:
                result += 1
        return result
        

        

        
# @lc code=end

