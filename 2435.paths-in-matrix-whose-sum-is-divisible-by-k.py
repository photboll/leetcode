#
# @lc app=leetcode id=2435 lang=python3
#
# [2435] Paths in Matrix Whose Sum Is Divisible by K
#

# @lc code=start

MOD = pow(10, 9) + 7
    
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        """
        grid of size m X n 
        length of each path is alwasys m + n - 1
        
        most likely a dp problem. we create subsoltion for the submatrices 1..m and 1..n 
        
        we need to keep track of the number of paths that end at each position for each sum (mod k)
        dp[i][j][s] will hold the number of paths that end at position i, j with the sum s.
        since we know that value at the current position we can calculate its contribution 

        Base case: any 1 X n or m X 1 grid will have only have a single path.
        grid[0][0] % k will give the index of wehre to put the one. all other paths in the base case have no solution

        """

        m = len(grid)
        n = len(grid[0])
        dp = [[[0]*k for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == 1 and j ==1:
                    dp[i][j][grid[0][0] % k] = 1
                    continue

                val = grid[i-1][j-1] % k
                for r in range(k):#each possible remainder
                    prev_mod = (r - val + k) % k
                    #we must have come from i-1 or j-1
                    dp[i][j][r] = (
                        dp[i-1][j][prev_mod] + #from i-1
                        dp[i][j-1][prev_mod]
                    ) % MOD
    
            
        return dp[m][n][0]
        
        
# @lc code=end

def print_3d(arr):
    for i in range(len(arr)):
        print()
        for j in range(len(arr[0])):
            print(tuple(arr[i][j]), end=" ")

if __name__ == "__main__":
    import local_testing
    sol = Solution()
    TEST_FILE = "2345aTest.txt"
    local_testing.run_tests(TEST_FILE, sol.numberOfPaths, max_test=100)