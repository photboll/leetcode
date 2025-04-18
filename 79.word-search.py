#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (44.79%)
# Likes:    16616
# Dislikes: 707
# Total Accepted:    2M
# Total Submissions: 4.5M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given an m x n grid of characters board and a string word, return true if
# word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# 
# Example 1:
# 
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCCED"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "SEE"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCB"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
# 
# 
# 
# Follow up: Could you use search pruning to make your solution faster with a
# larger board?
# 
#

# @lc code=start
from collections import deque, Counter
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def within_bounds(m, n, i, j):
    return 0 <= i < m and 0 <= j < n

def should_reverse(board, word):
    """
    if the count of the final char is smaller than the first letter, we should process it in reverse
    to prune the search tree
    """
    flattened = []
    for row in board:
        flattened.extend(row)
    counts = Counter(flattened)
    return counts[word[0]] > counts[word[-1]]

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Replaing the queue with a priority queue with th priority on th highest word_index would improve the 
        average runtime but when the word is present. knowing that the word is missing would still require to check the same amount of 
        nodes
        """
        m = len(board)
        n = len(board[0])
        len_word = len(word)
        if should_reverse(board, word):
            word = word[::-1]
            
        #Visited set is used to prevent self intersections, i.e. using the same position on the board for two different positions on the board 
        queue = deque()#(i, j, word_index_to_match, visited_set)
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    queue.append((i, j, 1, set([(i, j)])))
                 
        
        while queue :
            i, j, word_index, visited = queue.popleft()
            if word_index == len_word:
                #we have just traversed the whole word we are searching for
                #So it must exist in the board 
                return True
            #Check if any of the neighoboring cells contain the desired char  
            #In which case we add that position to the queue
            for di, dj in DIRECTIONS:
                ni, nj = i + di, j+dj
                if (within_bounds(m, n, ni, nj)
                    and board[ni][nj] == word[word_index]
                    and(ni, nj) not in visited):
                    visited_copy = visited.copy()
                    visited_copy.add((ni, nj))
                    queue.append((ni, nj, word_index + 1, visited_copy))
                    
        return False
# @lc code=end

