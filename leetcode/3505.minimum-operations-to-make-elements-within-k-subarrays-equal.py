# @lc app=leetcode id=3505 slug=minimum-operations-to-make-elements-within-k-subarrays-equal lang=python3
#
# [3505] Minimum Operations to Make Elements Within K Subarrays Equal
# Difficulty: Hard
# Tags: Array, Hash Table, Math, Dynamic Programming, Sliding Window, Heap (Priority Queue)
# URL: https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/
#
# @lc code=start

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        """
        find the median of each possible window of size x

        not good enough. the windows does not necessarily have to be alligned with start and end

        """


        cost = self.window_costs(nums, x)
        n = len(nums)

        INF = float("inf")
        prev = [0] * (n+1)

        for _ in range(k):
            cur = [INF] * (n+1)
            #for ecah possible end point of a window
            for i in range(x, n+1):
                #either
                cur[i] = min(cur[i-1], #skip this window
                             prev[i-x] + cost[i-x])# use this window)
            prev = cur
        return prev[n]

        
    def window_costs(self, nums, x):
        vals = sorted(set(nums))
        rank = {v: i+1 for i, v in enumerate(vals)}

        m = len(vals)
        cnt, sm = [0] * (m+1), [0] * (m+1)

        def add(v, sign):
            i = rank[v]
            while i <= m:
                cnt[i] += sign
                sm[i] += sign*v
                i += i & -i
        
        def kth(target):
            #rank of the target-th smallest element
            pos, step= 0, 1 << m.bit_length()
            while step:
                nxt = pos  + step
                if nxt <= m and cnt[nxt] < target:
                    pos, target = nxt, target - cnt[nxt]
                
                step >>= 1
            return pos + 1
        
        
        def prefix(i):
            c = s = 0
            while i:
                c += cnt[i]
                s += sm[i]
                i -= i & -i
            return c, s
        
        costs, total = [], 0
        for r, v in enumerate(nums):
            add(v, 1)
            total += v
            if r >= x:
                add(nums[r-x], -1)
                total -= nums[r-x]
            if r>= x -1:
                p = kth((x+1) // 2)
                med = vals[p-1]
                c, s = prefix(p)
                costs.append(med * c - s + (total -s) - med*(x - c))

        return costs 







        
        

# @lc code=end
