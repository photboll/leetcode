#
# @lc app=leetcode id=3474 lang=python3
#
# [3474] Lexicographically Smallest Generated String
#

# @lc code=start
class Solution:
    def generateString(self, s1: str, s2: str) -> str:
        """

        
        """
        n, m = len(s1), len(s2)

        size = n + m -1
        word = ["?"] * size

        # apply the matching constriant s1[] == "T"
        for i in range(n):
            if s1[i] == "T":
                for j in range(m):
                    if word[i + j] == "?":
                        word[i +j] = s2[j]

                    elif word[i+j] != s2[j]:
                        #impossible to satisfy conditions 
                        #char 
                        return ""
        
        word2 = word[:]

        #apply the "F" constrain

        for i in range(n):
            if s1[i] == "F":
                count_blank = 0
                count_same = 0
                last_blank = -1

                for j in range(m):
                    if word2[i + j] == "?":
                        if word[i+j] == "?":
                            word[i+j] = "a"
                        last_blank = i + j
                        count_blank += 1
                    
                    if word[i+j] == s2[j]:
                        count_same += 1
                if count_same == m and count_blank == 0:
                    return ""
                
                if count_same == m and count_blank > 0:
                    word[last_blank] = "b"

        return "".join(word)
                
                    
                    

        
        
# @lc code=end

