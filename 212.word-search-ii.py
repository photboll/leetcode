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
    def __init__(self, char=""):
        self.children = [None for _ in range(26)]
        self.is_terminal = False
        self.value = char
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        curr_node = self.root
        for char in key:
            char_i = ord(char) - ord("a")
            #Does a node exist for the current character
            if curr_node.children[char_i] == None:
                curr_node.children[char_i] = TrieNode(char=char)
        
            #move curr node forward to the new node
            curr_node = curr_node.children[char_i]
        curr_node.is_terminal = True
    
    def prefix_exists(self, prefix):
        curr_node = self.root
        for char in prefix:
            char_i = ord(char) - ord("a")
            if curr_node.children[char_i] is None:
                return False
            curr_node = curr_node.children[char_i]
            
        return True
    
    def search(self, key):
        curr_node = self.root
        for char in key:
            char_i = ord(char) - ord("a")
            if curr_node.children[char_i] is None:
                return False
            curr_node = curr_node.children[char_i]
        
        return curr_node.is_terminal
            
        
                
from collections import deque
def within_bounds(m, n, i, j):
    return 0 <= i < m and 0 <= j < n
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        We need to populate the trie by adding all non self-intersecting words present in the board to the trie
        
        """
        trie = Trie()
        m = len(board)
        n = len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        curr_word = []
        
        def backtrack(i, j):
            if len(curr_word) > 10:
                #words[i].length is constrain to be <= 10, so no need to consider any longer words
                return 
            trie.insert("".join(curr_word))
            
            for di, dj in DIRECTIONS:
                ni, nj = i + di, j+dj
                if not within_bounds(m, n, ni, nj) or visited[ni][nj]:
                    continue
                
                #Mark the next node as visited and append it to the current word
                visited[ni][nj] = True
                curr_word.append(board[ni][nj])
                backtrack(ni, nj)
                #Unmark the visited and remove the current letter
                curr_word.pop()
                visited[ni][nj] = False
        
        #The word can begin at any position 
        for i in range(m):
            for j in range(n):
                curr_word.append(board[i][j])
                visited[i][j] = True
                backtrack(i, j)
                curr_word.pop()
                visited[i][j] = False
        
        results = []
        for word in words:
            if trie.search(word):
                results.append(word)

        return results
            
                
                

class SolutionV1:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        We need to populate the trie by adding all non self-intersecting words present in the board to the trie
        
        """
        trie = Trie()
        queue = deque()# (i, j, word, visited_positions)
        m = len(board)
        n = len(board[0])
        #Words can start at any position in the board
        for i in range(m):
            for j in range(n):
                word = board[i][j]
                queue.append((i, j, word, set([(i, j)])))
                trie.insert(word)
        #print(queue)
        while queue:
            i, j, word, visited = queue.popleft()
            
            for di, dj in DIRECTIONS:
                ni, nj = i + di, j + dj
                if within_bounds(m,n,ni,nj) and (ni, nj) not in visited:
                    copy_visited = set(visited)
                    copy_visited.add((ni, nj))
                    new_word = word + board[ni][nj]
                    queue.append((ni, nj, new_word, copy_visited))
                    trie.insert(new_word)
        
        result = []
        for word in words:
            if trie.search(word):
                result.append(word)
        return result                
            
            
        
        
# @lc code=end

