#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
from collections import Counter

def atleast_count(counter1, counter2):
    """
    Returns true if the counter1 contains atleast the same amount for each key in counter2"""
    for char in counter2:
        if counter1[char] < counter2[char]:
            return False
    return True
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = Counter(t)
        inWindow = Counter()
        i = 0
        n = len(s)
        result = None 
        for j in range(n):
            #Expand the window
            char = s[j]
            inWindow[char] += 1
            #Do we have enough of char?
            if inWindow[char] < tCount[char]:
                continue
            
            #We do have enough of this char, Do we have enough of the other chars?
            #make the window smaller if we can 
            while i < j and inWindow[s[i]] > tCount[s[i]]:
                inWindow[s[i]] -= 1
                i+= 1
            
            if atleast_count(inWindow, tCount):
                if result is None or len(result) > j - i :
                    result = s[i:j+1]

        if result:
            return result
        else:
            return ""
                
                
            

            
        
# @lc code=end

