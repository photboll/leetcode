#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.isEndOfWord = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()       

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True

    def search(self, word: str) -> bool:
        return self._searchRecursive(self.root, word, 0)
            
    def _searchRecursive(self, node:TrieNode, word:str, i:int)-> bool :
        if i == len(word):
            return node.isEndOfWord
        
        char = word[i]

        if char == ".":
            for child in node.children.values():
                if self._searchRecursive(child, word, i + 1):
                    
                    return True
            return False

        if char not in node.children:
            return False

        return self._searchRecursive(node.children[char], word, i+1)
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

