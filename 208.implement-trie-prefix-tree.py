#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.isEndOfWord = False
        self.children = {}
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root 
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True

    def search(self, word: str) -> bool:
        node = self._findNode(word)
        return node is not None and node.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        return self._findNode(prefix) is not None

    def _findNode(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None 
            node = node.children[char]
        return node
    
    def delete(self, word:str)-> bool:
        return self._delete(self.root, word, 0)
    
    def _delete(self, node: TrieNode, word:str, depth: int)  -> bool:
        if depth == len(word):
            if not node.isEndOfWord:
                return False#Word does not exist
            node.isEndOfWord = False
            return len(node.children) == 0 
        
        char = word[depth]
        if char not in node.children:
            return False
        
        shouldDeleteChild = self._delete(node.children[char], word, depth + 1)

        if shouldDeleteChild:
            del node.children[char]
            return len(node.children)   == 0 and not node.isEndOfWord

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

