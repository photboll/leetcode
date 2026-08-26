#
# @lc app=leetcode id=3116 lang=python3
#
# [3116] Kth Smallest Amount With Single Denomination Combination
#

# @lc code=start
from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        coins.sort()

        def lcm(a, b):
            return a * b // gcd(a, b)
        
        subsets = [] # (lcm, sign)
        for mask in range(1, 1<<n):
            l = 1
            bits = 0
            overflow = False
            for i in range(n):
                if mask & (1 << i):
                    l = lcm(l, coins[i])
                    bits += 1
                    if l > (1 << 40):# cap to ovid overflow
                        overflow = True
                        break
            if overflow:
                subsets.append((None, bits))
            else:
                subsets.append((l, bits))
        
        def count_le(x):
            #count numbers <= x divisible by at least one coin
            total = 0 
            #inclusion-exclusion
            for l, bits in subsets:
                if l is None or l > x:
                    continue
                    
                sign = 1 if bits % 2 == 1 else -1
                total += sign * (x // l)
            return total
        
        
        # Binary search on the answer
        lo, hi = 1, min(coins) * k
        while lo < hi:
            mid = (lo + hi) // 2
            if count_le(mid) >= k:
                hi = mid
            else:
                lo = mid+1
        return lo

                    
        

        
# @lc code=end

