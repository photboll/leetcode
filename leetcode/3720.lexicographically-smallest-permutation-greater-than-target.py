# @lc app=leetcode id=3720 slug=lexicographically-smallest-permutation-greater-than-target lang=python3
#
# [3720] Lexicographically Smallest Permutation Greater Than Target
# Difficulty: Medium
# Tags: Hash Table, String, Greedy, Counting, Enumeration
# URL: https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/
#
# @lc code=start
from collections import Counter


class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freqs = Counter(s)
        result = []

        def backtrack(i, greater):
            #print(i, result)
            if i == n:
                candidate = "".join(result)
                return candidate if greater else ""
            
            for char in "abcdefghijklmnopqrstuvwxyz":
                if freqs[char] == 0:
                    continue
                
                if not greater and char < target[i]:
                    continue
                
                freqs[char] -= 1
                result.append(char)

                res = backtrack(i+1, greater or char > target[i])
                if res:
                    #early exit
                    return res

                result.pop()
                freqs[char] += 1

            return ""

        return backtrack(0, False)


        

# @lc code=end
