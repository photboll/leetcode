# @lc app=leetcode id=3734 slug=lexicographically-smallest-palindromic-permutation-greater-than-target lang=python3
#
# [3734] Lexicographically Smallest Palindromic Permutation Greater Than Target
# Difficulty: Hard
# Tags: Two Pointers, String, Enumeration
# URL: https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/
#
# @lc code=start
from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnts = [0] * 26
        for char in s:
            cnts[ord(char) - 97] += 1
        
        odd_letters = [i for i in range(26) if cnts[i] % 2 ==1]
        if n % 2 == 0:
            if odd_letters:
                return ""
            mid_char = ""
        else:
            if len(odd_letters) != 1:
                return ""
            mid_char = chr(97+odd_letters[0])
        
        
        
        half_counts = [cnts[i] // 2 for i in range(26)]

        h = n // 2
        T = target[:h]

        T_counts = [0] * 26
        for char in T:
            T_counts[ord(char) - 97] += 1
        
        if T_counts == half_counts:
            P = T + mid_char + T[::-1]
            if P > target:
                return P
        
        
        counts = half_counts[:]
        best = None
        for i in range(h):
            idx_T = ord(T[i]) - 97
            found = None
            for letter in range(idx_T+1, 26):
                if counts[letter] > 0:
                    found = letter
                    break
            
            if found is not None:
                new_counts = counts[:]
                new_counts[found] -= 1
                suffix = ''.join(chr(97+k)*new_counts[k] for k in range(26) if new_counts[k] > 0)
                best = T[:i] + chr(97+found) + suffix
            if counts[idx_T] > 0:
                counts[idx_T] -= 1
            else:
                break
        
        if best is not None:
            return best + mid_char + best[::-1]
        return ""


            

        


        
        

# @lc code=end
