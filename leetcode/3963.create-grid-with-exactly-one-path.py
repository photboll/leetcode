# @lc app=leetcode id=3963 slug=create-grid-with-exactly-one-path lang=python3
#
# [3963] Create Grid With Exactly One Path
# Difficulty: Easy
# Tags: None
# URL: https://leetcode.com/problems/create-grid-with-exactly-one-path/
#
# @lc code=start
class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        result = []
        result.append("."*n)

        for _ in range(1, m):
            result.append("#"*(n-1)+".")
        return result
        

        

# @lc code=end
