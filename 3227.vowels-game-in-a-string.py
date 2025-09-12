#
# @lc app=leetcode id=3227 lang=python3
#
# [3227] Vowels Game in a String
#

# @lc code=start
VOWELS = set(c for c in "aeiou")
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        """
        This setup is similar to the game of Nim. 
        In Nim the winner is already decided upon the start of the game (provided they play optimally)
        
        This is avariation, since the end criteria is different for the two participants.
        
        If the string have no vowels, only Bob can make a move. Then Bob wins.
        
        if the string contains an even number of vowels on Bobs turn, then bob should remove all vowels.
        forcing Alice to lose since she can only act if there are any vowels left
        
        if the string contains an even number of vowels on Alices turn, then Alice should leave a single vowel.
        forcing Bob to remove only consonants. then Alice can remove the entire string on her following turn.
        Forcing Bob to lose. 
        """
        vowel_count = 0
        for c in s:
            if c in VOWELS:
                vowel_count += 1
        
        if vowel_count == 0:
            return False
        else: 
            return True

        
# @lc code=end

