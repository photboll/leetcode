#
# @lc app=leetcode id=1358 lang=python3
#
# [1358] Number of Substrings Containing All Three Characters
#

# @lc code=start
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        #Sliding window
        #iterate for each possible end position r
        #l = the minumium index of all possible chars will give the left endpoint
        #all substrings starting from 0 to l and ending at r 
        # holds the last occurence of each char in the window 

        last = {"a":-1, "b":-1, "c":-1}
        n = len(s)
        result = 0

        for i, r in enumerate(range(n)):
            last[s[r]] = i
            min_last = r

            for char in last:
                min_last = min(last[char],min_last)
            
            if min_last < 0:
                continue

            result += min_last + 1
        return result
            
            
            

        
# @lc code=end

