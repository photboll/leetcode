# @lc app=leetcode id=2381 slug=shifting-letters-ii lang=python3
#
# [2381] Shifting Letters II
# Difficulty: Medium
# Tags: Array, String, Prefix Sum
# URL: https://leetcode.com/problems/shifting-letters-ii/
#
# @lc code=start
from string import ascii_lowercase
int_a = ord("a")
ALPHABET_SIZE = len(ascii_lowercase)

class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        i_chars = [ord(c) - int_a for c in s]
        diffs = [0] * n

        print(i_chars)
        for start, end, dir in shifts:
            dir = dir if dir == 1 else -1
            diffs[start] += dir
            if end+1 < n:
                diffs[end+1] -= dir

        print(diffs)
        num_shifts = 0
        for i in range(n):
            num_shifts = (num_shifts + diffs[i] + ALPHABET_SIZE) % ALPHABET_SIZE
            i_chars[i] = (i_chars[i] + num_shifts + ALPHABET_SIZE) % ALPHABET_SIZE
            
        
        return "".join(map(lambda c: chr(c+int_a), i_chars))
            


        

# @lc code=end
