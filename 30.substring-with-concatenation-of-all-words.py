#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
from collections import Counter
class Solution:
    #This solution will probably run into TLE 
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        #The problem statement says that all words are of the same length 
        #Which simplifies the sliding of the window
        #Example 2 shows a case where we have a duplicate in word. so duplicate are allowed,
        #Example 3 shows one were the strings are overlapping each other 
        len_words = len(words)
        word_len = len(words[0]) # Determines the step size of the sliding window 
        result = [] #Will hold the starting index of each concatenated string 
        #The window will have a fixed size of len_words * word_len 
        #Since a concatenated string contains every word once
        #We will maintain two counters, one which keeps the target of the counts for the concatenated string
        #The other one will contain the current words in the window
        #When the counts match we have found an index
        len_target = len_words * word_len
        target = Counter(words)
        in_window = Counter()
        n = len(s)
        for start in range(n):
            if start + len_target > n:
                continue
            
            in_window.clear()
            for i in range(start, start+len_target, word_len):
                in_window[s[i:i+word_len]] += 1
            #Check if in_winodw contains the same counts as target
            if len(target - in_window) == 0:
                result.append(start)
                
        return result
                    
                
            
            
        
# @lc code=end


