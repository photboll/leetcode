#
# @lc app=leetcode id=1930 lang=python3
#
# [1930] Unique Length-3 Palindromic Subsequences
#

# @lc code=start
from collections import Counter
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        palindromes = set()
        #holds all chars that is left of the current
        l_chars = set()
        #Holds the frequency of each char to the right of current
        r_freqs = Counter(s)

        
        for i in range(len(s)):
            curr = s[i]

            r_freqs[curr] -= 1
            if r_freqs[curr] == 0:
                del r_freqs[curr]
            
            for outer in l_chars:
                if outer in r_freqs:
                    #then we have a palindrome outer curr outer
                    palindromes.add((outer, curr))
            l_chars.add(curr)

        return len(palindromes)
                    
            
        
class SolutionWRONG:
    def countPalindromicSubsequence(self, s: str) -> int:
        """
        there are 26 * 26 possible 3 length palindromes.
        it is necessary that one of the characters occurs twic e in sthe string 
        keep track of the start and end occurence of each char.
        then we can check for each pair of chars. if their intervals overlap we can 
        make a palindrome 
        """
        start = {}
        end = {}
        freqs = Counter()
        for i, c in enumerate(s):
            freqs[c] += 1
            if c not in start:
                start[c] = i
                end[c] = i
            else:
                end[c] = i

        result = 0
        print(start)
        print(end)

        chars = list(freqs.keys())
        n = len(chars)
        for i in range(n):
            a = chars[i]
            #palindromes of the form aaa
            if freqs[a] > 2:
                result += 1
            for j in range(i+1, n):
                b = chars[j]
                #intervals need to overlap
                if (start[a] <= end[b] and
                      start[b] <= end[a]):
                    result += (freqs[a] > 1) #aba
                    result += (freqs[b] > 1) #bab
        return result 
                

        



        
# @lc code=end

