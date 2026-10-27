# @lc app=leetcode id=3619 slug=count-islands-with-total-value-divisible-by-k lang=python3
#
# [3619] Count Islands With Total Value Divisible by K
# Difficulty: Medium
# Tags: Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix
# URL: https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/
#
# @lc code=start
DIRECTIONS  = [(1,0), (-1, 0), (0, 1), (0,-1)]
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        answer = 0
        stack = []
        visited = [[False]*n for _ in range(m)]

        
        for i in range(m):
            for j in range(n):
                if visited[i][j] or grid[i][j] == 0:
                    continue

                # Current position is land 
                visited[i][j] = True
                stack.append((i, j))
                cur_sum = 0

                while stack:
                    cur_i, cur_j = stack.pop()
                    cur_sum += grid[cur_i][cur_j]

                    for di, dj in DIRECTIONS:
                        ni, nj = cur_i + di, cur_j + dj
                        #within bounds not visited and is land
                        if (0 <= ni < m and 0 <= nj < n) and not visited[ni][nj] and grid[ni][nj]> 0:
                            visited[ni][nj] = True
                            stack.append((ni, nj))
                
                if cur_sum % k == 0:
                    answer += 1

        return answer




# @lc code=end
