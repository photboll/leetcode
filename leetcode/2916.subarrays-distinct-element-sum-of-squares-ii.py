# @lc app=leetcode id=2916 slug=subarrays-distinct-element-sum-of-squares-ii lang=python3
#
# [2916] Subarrays Distinct Element Sum of Squares II
# Difficulty: Hard
# Tags: Array, Hash Table, Binary Indexed Tree, Segment Tree
# URL: https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/
#
# @lc code=start
MOD = pow(10, 9) + 7

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)

        s1 = [0] *(4 * n)
        s2 = [0] *(4 * n)
        lz = [0] *(4 * n)
        
        def apply(o, length, v):
            s2[o] = (s2[o] + 2 * v * s1[o] + length * v * v) % MOD
            s1[o] = (s1[o] + length * v)  % MOD
            lz[o] += v
        
        def push(o, l, r):
            if lz[o]:
                m = (l+r) // 2
                apply(2 *o, m-l+1, lz[o])
                apply(2*o+1, r-m, lz[o])
                lz[o] = 0
        
        def update(o, l, r, ql, qr):
            if ql <= l and r <= qr:
                apply(o, r-l+1, 1)
                return

            push(o, l, r)
            m = (l + r)//2
            if ql <= m:
                update(2 *o, l, m, ql, qr)

                
            if qr > m:
                update(2 * o+1, m+1, r, ql, qr)

            s1[o] = (s1[2*o] + s1[2*o+1]) % MOD
            s2[o] = (s2[2*o] + s2[2*o+1]) % MOD
        
        last = {}
        ans = 0
        for i, x in enumerate(nums):
            p = last.get(x, -1)
            update(1, 0, n-1, p+1, i)
            last[x] = i
            ans = (ans+s2[1]) % MOD
        return ans
                
            

        

# @lc code=end
