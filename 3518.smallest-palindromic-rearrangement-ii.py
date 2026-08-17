#
# @lc app=leetcode id=3518 lang=python3
#
# [3518] Smallest Palindromic Rearrangement II
#

# @lc code=start
from collections import Counter
from math import comb
class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        counts = Counter(s[:n//2])
        mid = s[n//2] if n % 2 else ""

        def total_arrangements(freqs, cap):
            result, placed = 1, 0
            for c in freqs.values():
                if c:
                    result *= comb(placed+ c, c)
                    placed += c
                    if result > cap:
                        return result
            return result
        
        if k > total_arrangements(counts, k+1):
            return ""

        remaining = dict(counts)
        prefix = []
        for _ in range(n // 2):
            for char in "abcdefghijklmnopqrstuvwxyz":
                if remaining.get(char, 0) == 0:
                    continue

                remaining[char] -= 1
                cnt = total_arrangements(remaining, k+1)
                if cnt >= k:
                    prefix.append(char)
                    break
                k -= cnt
                remaining[char] += 1
            
        prefix = "".join(prefix)
        return prefix + mid + prefix[::-1]




        
# @lc code=end

