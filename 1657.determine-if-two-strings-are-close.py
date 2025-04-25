#
# @lc app=leetcode id=1657 lang=python3
#
# [1657] Determine if Two Strings Are Close
#

# @lc code=start
from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        #Since we can swap to arbitrary chars there is no need to consider the ordering of each string
        #So we can simply operate on the frequency counts 
        # Both word2 needs to have every unique character from word1 in it, else operation 2 can never reach the missing char
        # the mulitplicity of the frequency counts of both words needs to match 
        if set(word1) != set(word2):
            #Both words must contain the samw unique chars
            return False
        counts1 = Counter(word1)
        counts2 = Counter(word2)
        
        for freq1, freq2 in zip(sorted(counts1.values()), sorted(counts2.values())):
            if freq1 != freq2:
                return False
        return True       

        
# @lc code=end

