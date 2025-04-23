#
# @lc app=leetcode id=2131 lang=python3
#
# [2131] Longest Palindrome by Concatenating Two Letter Words
#

# @lc code=start
from collections import Counter
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        """
        The words will always have an even length 
        It can consist of either an even number of pairs or an odd number 
        if it is an odd number of pairs then the middle word must be a palindrome itself 
        Can there be duplicate words in the input?, yes it is possible example two have two words of "ab"
        I think we will have too handle palindromic words themselves seperately.
        What matters for two non-palindromic words to be apble to be concatenate?
        if the reverse word is not present in the list, then it will never be in any concatenate palindrome 
        how do we handle when there might be different counts ["lc", "cl", "lc", "cl", "lc"]? must not forget repeating if possible
        
        """
        count = Counter(words)
        longestPalindrome = 0
        can_add_palindromic_word = False
        for w in words:
            #Have we already used up all ws  
            if count[w] == 0:
                continue
            
            rev_w = w[::-1]
            #special case when w == rev_w and we only have a single example   
            if rev_w == w and count[w] == 1:
                #Then it must be put in the middle of the concatenated word 
                #And there is only one middle, so it can happen at most once
                can_add_palindromic_word = True
            #Is its palindrome in words?
            elif count[rev_w] > 0:
                #then w and rev_w can be added to the concatenated word
                count[w] -= 1
                count[rev_w] -= 1
                longestPalindrome += 4
            
        if can_add_palindromic_word:
            longestPalindrome += 2
            
        return longestPalindrome
        
# @lc code=end

