#
# @lc app=leetcode id=3304 lang=python3
#
# [3304] Find the K-th Character in String Game I
#

# @lc code=start

def alice_op(word):
    new_word = [0] * len(word)
    for i in range(len(word)):

        new_word[i] = chr((ord(word[i]) - ord("a") + 1) % 25 + ord("a"))
    return word + "".join(new_word)
class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) < k:
            #print(word)
            word = alice_op(word)

        return word[k-1]
        
# @lc code=end

