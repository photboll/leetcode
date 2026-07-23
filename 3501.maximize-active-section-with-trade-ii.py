#
# @lc app=leetcode id=3501 lang=python3
#
# [3501] Maximize Active Section with Trade II
#

# @lc code=start
from bisect import bisect_right

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)

        segments, total_s, curr_type, curr_start = [], 0, s[0], 0
        for i in range(1, n):
            if s[i] != curr_type:
                slen = i - curr_start
                segments.append((curr_start, i-1, curr_type, slen))
                if curr_type == '1': total_s += slen
                curr_type, curr_start = s[i], i
        slen = n - curr_start
        segments.append((curr_start, n-1, curr_type, slen))
        if curr_type == '1': total_s += slen
                
        m = len(segments)
        g = [0] * m
        for j in range(1, m - 1):
            if segments[j][2] == '1':
                g[j] = segments[j-1][3] + segments[j+1][3]
        
        st_size = 1
        while st_size < m: st_size *= 2
        tree = [0] * (2 * st_size)
        for i in range(m): tree[st_size + i] = g[i]
        for i in range(st_size - 1, 0, -1): tree[i] = max(tree[2 * i], tree[2 * i + 1])
                
        def st_query(ql, qr):
            res = 0
            ql, qr = ql + st_size, qr + st_size
            while ql < qr:
                if ql & 1: res = max(res, tree[ql]); ql += 1
                if qr & 1: qr -= 1; res = max(res, tree[qr])
                ql, qr = ql >> 1, qr >> 1
            return res

        starts, results = [seg[0] for seg in segments], []

        for l, r in queries:
            a, b, max_g = bisect_right(starts, l) - 1, bisect_right(starts, r) - 1, 0
            if a < b:
                j = a + 1
                if j < b and segments[j][2] == '1' and segments[a][2] == '0':
                    if j + 1 < b or (j + 1 == b and segments[b][2] == '0'):
                        ll = segments[a][1] - l + 1
                        rr = segments[j+1][3] if j + 1 < b else (r - segments[b][0] + 1)
                        max_g = max(max_g, ll + rr)
                j = b - 1
                if j > a + 1 and segments[j][2] == '1' and segments[b][2] == '0':
                    ll, rr = segments[j-1][3], r - segments[b][0] + 1
                    max_g = max(max_g, ll + rr)
                if a + 2 <= b - 2:
                    max_g = max(max_g, st_query(a+2, b-1))
            results.append(total_s + max_g)
        
        return results
            
# @lc code=end

