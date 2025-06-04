#
# @lc app=leetcode id=3403 lang=python3
#
# [3403] Find the Lexicographically Largest String From the Box I
#

# @lc code=start


class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)
        if numFriends == 1:
            return word
        
        largest_char = sorted(list(set(word)))[-1]
        
        largest_str = ""
        for l in range(n):
            if word[l] != largest_char:
                continue

            for size in range(1,min(n-numFriends+1, n-l)+1):
                cur_str = word[l:l+size]
                if cur_str > largest_str:
                    largest_str = cur_str
        
        return largest_str
               
        
        
# @lc code=end

