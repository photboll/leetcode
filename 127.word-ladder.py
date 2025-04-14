#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start

from collections import deque, defaultdict
def is_word_neighbors(w1, w2):
    count = 0
    for i in range(len(w1)):
       if w1[i] != w2[i]:
           count += 1
           if count > 1:
               return False
    return True

def get_word_neighbors(words):
    n = len(words)
    edges = defaultdict(list)
    for i in range(n):
        for j in range(i+1, n):
            if is_word_neighbors(words[i], words[j]):
                edges[words[i]].append(words[j])
                edges[words[j]].append(words[i])
                
    return edges

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Find which words only differ in a single letter, build the graph
        use bfs to travers it 
        """
        neighbors = get_word_neighbors(wordList)
        
        if endWord not in wordList:
            return 0
        
        #Since begin word did not have to exist in the wordlist 
        #we need to add it to the nieghbors dict seperately 
        for word in wordList:
            if is_word_neighbors(beginWord, word):
                neighbors[beginWord].append(word)
                
        visited = set()
        queue = deque()
        
        queue.append((beginWord, 1))# (Current word, lenght of transformation sequence)
        visited.add(beginWord)
        while queue:
            curr_word, curr_len = queue.popleft()
            if curr_word == endWord:
                return curr_len
            
            for next_word in neighbors[curr_word]:
                if next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, curr_len+1)) 
        
        return 0
        
# @lc code=end

