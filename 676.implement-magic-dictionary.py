#
# @lc app=leetcode id=676 lang=python3
#
# [676] Implement Magic Dictionary
#

# @lc code=start
def word_to_candidates(word):
    for i in range(len(word)):
        yield word[:i] + word[i:]
    
class MagicDictionary:

    def __init__(self):
        self.dict = set()
        

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            for curr in word_to_candidates(word):
                self.dict.add(curr)
        

    def search(self, searchWord: str) -> bool:
        for curr in word_to_candidates(searchWord):
            if curr in self.dict:
                return True
        return False
        

        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
# @lc code=end

