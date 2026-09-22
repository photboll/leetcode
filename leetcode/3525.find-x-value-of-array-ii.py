# @lc app=leetcode id=3525 slug=find-x-value-of-array-ii lang=python3
#
# [3525] Find X Value of Array II
# Difficulty: Hard
# Tags: Array, Math, Segment Tree
# URL: https://leetcode.com/problems/find-x-value-of-array-ii/
#
# @lc code=start
from typing import List

class SegTree:
    def __init__(self, nums: List[int], k: int):
        self.n = len(nums)
        self.k = k
        size = 4 * self.n
        self.cnt = [None] * size
        self.prod = [0] * size
        self._build(1, 0, self.n - 1, nums)

    def _merge(self, lc, lp, rc, rp):
        k = self.k
        res = lc[:]  # prefixes fully inside left child
        for r in range(k):
            c = rc[r]
            if c:
                idx = (lp * r) % k
                res[idx] += c
        return res, (lp * rp) % k

    def _build(self, node, l, r, nums):
        if l == r:
            v = nums[l] % self.k
            c = [0] * self.k
            c[v] = 1
            self.cnt[node] = c
            self.prod[node] = v
            return
        mid = (l + r) // 2
        self._build(2 * node, l, mid, nums)
        self._build(2 * node + 1, mid + 1, r, nums)
        self._pull(node)

    def _pull(self, node):
        c, p = self._merge(self.cnt[2 * node], self.prod[2 * node],
                            self.cnt[2 * node + 1], self.prod[2 * node + 1])
        self.cnt[node] = c
        self.prod[node] = p

    def update(self, node, l, r, idx, val):
        if l == r:
            v = val % self.k
            c = [0] * self.k
            c[v] = 1
            self.cnt[node] = c
            self.prod[node] = v
            return
        mid = (l + r) // 2
        if idx <= mid:
            self.update(2 * node, l, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, r, idx, val)
        self._pull(node)

    def query(self, node, l, r, ql, qr):
        if qr < l or r < ql:
            return None
        if ql <= l and r <= qr:
            return (self.cnt[node], self.prod[node])
        mid = (l + r) // 2
        left = self.query(2 * node, l, mid, ql, qr)
        right = self.query(2 * node + 1, mid + 1, r, ql, qr)
        if left is None:
            return right
        if right is None:
            return left
        return self._merge(left[0], left[1], right[0], right[1])


class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        st = SegTree(nums, k)
        ans = []
        for index, value, start, x in queries:
            st.update(1, 0, n - 1, index, value)
            c, _ = st.query(1, 0, n - 1, start, n - 1)
            ans.append(c[x])
        return ans


# @lc code=end
