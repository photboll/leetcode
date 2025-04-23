#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
# https://leetcode.com/problems/word-search-ii/description/
#
# algorithms
# Hard (37.09%)
# Likes:    9768
# Dislikes: 489
# Total Accepted:    775.3K
# Total Submissions: 2.1M
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' +
#["oath","pea","eat","rain"]'
#
# Given an m x n board of characters and a list of strings words, return all
# words on the board.
# 
# Each word must be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once in a word.
# 
# 
# Example 1:
# 
# 
# Input: board =
# [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
# words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
# 
# 
# Example 2:
# 
# 
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 10^4
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.
# 
# 
#

# @lc code=start
DIRECTIONS = [(0,1), (0, -1), (1, 0), (-1, 0)]
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode()
            #move curr node forward to the new node
            curr_node = curr_node.children[char]
        curr_node.word = word
            
        
                
from collections import deque
def within_bounds(m, n, i, j):
    return 0 <= i < m and 0 <= j < n
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        We need to populate the trie by adding all non self-intersecting words present in the board to the trie
        
        """
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        m = len(board)
        n = len(board[0])
        result = []
        visited = [[False] * n for _ in range(m)]
        
        def dfs(i, j, curr_node):
            char = board[i][j]

            if char not in curr_node.children:
                return 
            
            next_node = curr_node.children[char]
            if next_node.word:
                result.append(next_node.word)
                next_node.word = None#Prune to skip adding the same word multiple times 
            
            visited[i][j] = True
            for di, dj in DIRECTIONS:
                ni, nj = i + di, j+dj
                if within_bounds(m, n, ni, nj) and not visited[ni][nj]:
                    dfs(ni, nj, next_node)
            #Backtrack
            visited[i][j] = False
        
        for start_i in range(m):
            for start_j in range(n):
                dfs(start_i, start_j, trie.root)
        
        return result    
        
        
# @lc code=end

