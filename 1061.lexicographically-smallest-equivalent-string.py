#
# @lc app=leetcode id=1061 lang=python3
#
# [1061] Lexicographically Smallest Equivalent String
#

# @lc code=start
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # parent[i] stores the representative of the set containing character i
        # We use integers 0-25 to represent 'a'-'z'
        parent = list(range(26))

        # The find function returns the representative of the set for element i.
        # It uses path compression for optimization.
        def find(i: int) -> int:
            if parent[i] == i:
                return i
            # Path compression: set parent directly to the root
            parent[i] = find(parent[i])
            return parent[i]

        # The union function merges the sets containing elements i and j.
        def union(i: int, j: int):
            root_i = find(i)
            root_j = find(j)
            
            if root_i == root_j:
                return

            # To get the lexicographically smallest representative,
            # we always make the smaller character the parent.
            if root_i < root_j:
                parent[root_j] = root_i
            else:
                parent[root_i] = root_j

        # 1. Process all equivalences from s1 and s2 to build the sets
        for i in range(len(s1)):
            char1_idx = ord(s1[i]) - ord('a')
            char2_idx = ord(s2[i]) - ord('a')
            union(char1_idx, char2_idx)

        # 2. Build the result string using the generated equivalences
        result = []
        for char in baseStr:
            char_idx = ord(char) - ord('a')
            # Find the smallest character in the current character's set
            root_idx = find(char_idx)
            # Append the smallest equivalent character to the result
            result.append(chr(root_idx + ord('a')))
            
        return "".join(result)
        
# @lc code=end

