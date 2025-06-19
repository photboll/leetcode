#
# @lc app=leetcode id=3085 lang=python3
#
# [3085] Minimum Deletions to Make String K-Special
#

# @lc code=start
from collections import Counter
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        """
        The indices i and j seems to be redundant. the freqency of each unique char is what matters
        not their position.
        We want to minimize the number of deletions. Can we simply brute force it?
        for each unique digit 
        
        """
        counter = Counter(word)
        freqs = list(counter.items())
        
        min_deletions = float("inf")
        for i in range(len(freqs)):
            _, x = freqs[i]
            total_deletions = 0
            for j in range(len(freqs)):
                if i == j: continue
                #3 cases. x is the count of freqs[i] and y is the count of freqs[j]
                #1. if y < x then all occurences of ys char need to be deleted: else x would not be the min candidate
                #2. if y > x + k then we need to delete y - x -k to not break the k-speciality
                #3. x <=  y <= x + k: then nothing needs to be deleted. y have no effect on the k-speciality of the string
                _, y = freqs[j]
                if y < x:
                    total_deletions += y
                elif y > x + k:
                    total_deletions += y - x-k
            
            min_deletions = min(min_deletions, total_deletions)
        return min_deletions
            
                
                
                
            
            

        
# @lc code=end

