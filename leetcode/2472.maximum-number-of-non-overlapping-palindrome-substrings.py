# @lc app=leetcode id=2472 slug=maximum-number-of-non-overlapping-palindrome-substrings lang=python3
#
# [2472] Maximum Number of Non-overlapping Palindrome Substrings
# Difficulty: Hard
# Tags: Two Pointers, String, Dynamic Programming, Greedy
# URL: https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/
#
# @lc code=start

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        """
        is there any circumstance where it would be beneficial to not use the first palindrome
        satisfying the criteria? i.e. can we be greedy?

        s = "abaccdbbd", k = 3
        
        aba is one. it ends at position 2 (inclusive)

        maxPalindromes(s[2:], k) + 
        
        Any palindrome of length > k+1 will contain a substring that is itself palindromic of length k or k+1 (depending on even/odd)
        
        """

        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

            
        n = len(s)
        result = 0
        prev = 0

        for r in range(k-1, n):
            l = r - k + 1
            if (   l >= prev and isPalindrome(l, r) or 
                (l-1 >= prev and isPalindrome(l-1, r))):
                print(l, r, s[l:r+1],s[l:r+1] == s[l:r+1][::-1], s[l:r+1][::-1])
                result += 1
                prev = r + 1
        
        return result 

        
        

# @lc code=end
