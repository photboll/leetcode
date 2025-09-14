#
# @lc app=leetcode id=966 lang=python3
#
# [966] Vowel Spellchecker
#

# @lc code=start

#We map all vowels to a vowel wildcard
VOWELS = {c for c in "aeiou"}

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        """
        Go through the wordlist and create the mappings.
        can I do all cass from a single map?
        """
        word_exact = {}
        word_cap= {}
        word_vow = {}
        
        def get_vowel_rep(word):
            return "".join("*" if c in VOWELS else c for c in word)

        for word in wordlist:
            word_lower = word.lower()
            word_exact[word]  = word
            word_cap.setdefault(word_lower, word)
            word_vow.setdefault(get_vowel_rep(word_lower), word)
            
        
        
        result = []
        for q in queries:
            if q in word_exact:
                result.append(word_exact[q])
                continue
            elif q.lower() in word_cap:
                result.append(word_cap[q.lower()])
                continue
            rep = get_vowel_rep(q.lower())
            if rep in word_vow:
                result.append(word_vow[rep])
            else:
                result.append("")
            
        return result
            
            
        
        
        
        
# @lc code=end

