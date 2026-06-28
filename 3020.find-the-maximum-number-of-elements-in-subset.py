#
# @lc app=leetcode id=3020 lang=python3
#
# [3020] Find the Maximum Number of Elements in Subset
#

# @lc code=start
from collections import Counter
from math import isqrt

class Solution:
    def maximumLength(self, nums):
        freq = Counter(nums)
        
        one_cnt = freq.get(1, 0)
        ans = one_cnt if one_cnt % 2 else one_cnt -1

        freq.pop(1, None)

        for num in freq:
            res = 0
            x = num
            while x in freq and freq[x] > 1:
                res += 2
                x *= x
            ans = max(ans, res + (1 if x in freq else -1))
        return ans 
                

class Solutionv1:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)
        
        # 1s: pick largest odd count <= freq[1]
        res = 0
        if freq[1] > 0:
            res = freq[1] if freq[1] % 2 == 1 else freq[1] - 1
        
        for x in freq:
            if x == 1:
                continue
            # Skip perfect squares — they'll be covered when iterating their square root
            sq = isqrt(x)
            if sq * sq == x and sq in freq:
                continue
            
            n = 0
            cur = x
            while cur <= 10**9 and freq[cur] >= 2:
                n += 2
                cur = cur * cur
            
            # cur is now the candidate middle element
            if cur in freq:
                n += 1  # use as middle
            else:
                n -= 1  # remove one from the outermost pair (make it the new middle)
            
            res = max(res, n)
        
        return res

class Solutionv1:
    def maximumLength(self, nums: List[int]) -> int:

        freq = Counter(nums)

        res = 1 if freq[1] > 0 else 0

        for f in freq:
            x = f
            sq = isqrt(x)

            if sq * sq == x and freq[sq] > 1:
                continue

            n = 0
            while x < 31623 and freq[x] > 1:
                n += 2
                x *= x

            res = max(res, n + ((x in freq) << 1) -1)

        return res
        
# @lc code=end

