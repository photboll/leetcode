#
# @lc app=leetcode id=2573 lang=python3
#
# [2573] Find the String with LCP
#

# @lc code=start
from typing import List

def build_suffix_array(s):
    arr = []
    for i in range(len(s) -1 , -1, -1):
        suffix = s[i:]
        arr.append((suffix, i))
    
    arr.sort()
    #print(arr)
    return [val[1] for val in arr]

def build_lcp_array(s, suffix_array):
    n = len(s)
    #rank : inversa of suffix_array : maps suffix -> its sorted position
    rank = [0] * n # rank[i] = position of suffix i in suffix array
    lcp = [0] * n

    for i, suffix in enumerate(suffix_array):
        rank[suffix] = i
    
    h = 0 # current LCP length
    for i in range(n):
        if rank[i] > 0:
            j = suffix_array[rank[i] - 1]# previous suffix in sorted order
            while i + h < n and j + h < n and s[i+h] == s[j+h]:
                h += 1
            
            lcp[rank[i]] = h
            if h > 0:
                h -= 1
    return lcp


class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        for i in range(n):
            if lcp[i][i] != n-i:
                return ""

        
        #greedily build a candidate word
        word = ["?"] * n
        c = ord("a")
        for i in range(n):
            if word[i] == "?":
                #not enough characters to construct a string
                if c > ord("z"):
                    return ""
                
                word[i] = chr(c)
                for j in range(i+1, n):
                    if lcp[i][j] > 0:
                        word[j] = chr(c)
                c += 1
        
        print(f"{lcp=}")
        print(f"{word=}")


        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word[i] != word[j]:
                    if lcp[i][j]:
                        return ""
                else:
                    if i == n-1 or j == n-1:
                        if lcp[i][j] != 1:
                            return ""
                    else:
                        if lcp[i][j] != lcp[i+1][j+1] + 1:
                            return ""

        
        return "".join(word)
            
            


        
# @lc code=end


if __name__ == "__main__":
    s = "banana"
    suff_arr = build_suffix_array(s)
    print(f"{suff_arr=}")
    lcp_arr = build_lcp_array(s, suff_arr)
    print(f"{lcp_arr=}")




    
