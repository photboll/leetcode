#
# @lc app=leetcode id=820 lang=python3
#
# [820] Short Encoding of Words
#

# @lc code=start
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        """
        build a Trie backwards 
        em is a substring of emit which s why they can be encoded into one
        since we use a stop char # and we can only have one index per word
        any string that is a substring of another string is only useful if 
        they are alligned with each other at the end 

        if we would have ad two indices per word we could skip the # and all substrings would be useful 
        
        we dont actually have to build the references string.
        we only needs to determine its length 
        which means that we dont actually need to keep track of where each word is 
        any word that is a suffix of another can be ommited from the reference string
        """
        S = set(words)
        for word in words:
            #each possible starting point of a suffix
            #remove each proper suffix 
            for i in range(1, len(word)):
                suffix = word[i:]
                S.discard(suffix)
        
        res = 0
        for word in S:
            res += len(word) + 1#
        return res


        
# @lc code=end

