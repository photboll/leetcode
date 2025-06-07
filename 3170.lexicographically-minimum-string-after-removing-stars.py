#
# @lc app=leetcode id=3170 lang=python3
#
# [3170] Lexicographically Minimum String After Removing Stars
#

# @lc code=start
from heapq import heappop, heappush
NONE_TOKEN = "<DELETED>"
class Solution:
    def clearStars(self, s: str) -> str:
        """
        In the case of ties of smallest character, the right most one should be remove
        SInce it affects the lexicographicall ordering the least
        it is not sufficient to keep track of the current smallest char, 
        in case we encounter mulitple * in a row 
        can we use a heap:
        each character we see we push (char, index) to the heap]
        when encountering a * we pop from the heap and marks the char at index as deleted
        """
        chars = [c for c in s]
        pq = []
        for i, char in enumerate(chars):
            if char == "*":
                #Rember pq holds the negative of the index,
                _, j = heappop(pq)
                chars[-j] = NONE_TOKEN# Remove the smallest char
                chars[i] = NONE_TOKEN # Remove the *
            else:
                #Heappush presumes a min heap
                #Negate i to get maxHeap behavior
                heappush(pq, (char, -i))
        
        #print(chars)
                
        res = []
        for token in chars:
            if token != NONE_TOKEN:
                res.append(token)
        
        return "".join(res)
        
        
# @lc code=end

