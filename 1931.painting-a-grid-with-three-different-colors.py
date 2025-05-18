#
# @lc app=leetcode id=1931 lang=python3
#
# [1931] Painting a Grid With Three Different Colors
#

# @lc code=start
from collections import defaultdict
MOD = pow(10, 9) + 7
def get_valid_coloring(n, num_colors=3):
    
    result = []
    coloring = []
    def backtrack(prev_color):
        #print(coloring)
        if len(coloring) == n:
            result.append(tuple(coloring))
            return 
        
        for color in range(num_colors):
            if color != prev_color:
                coloring.append(color)
                backtrack(color)
                coloring.pop()
    
    backtrack(-1)#-1 No previous color used, starting at -1
    return result
        
def can_transition(state1, state2) -> bool:
    for s1, s2 in zip(state1, state2):
        if s1 == s2:
            return False
    return True
        
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        """
        Dp problem with bit masking columns. m is size of column.
        Three colors to choose from 

        is adjacent including both left-right and up-down or is it only left-right?
        
        Lets start with a single column of length 5.
        The first row can be chosen in 3 ways  R, G, or B 
        row 2: 2 choices any of those not chosen in row first
        ro2 3:5 2 choices same reason as row 2.
        3 * 2**4 = 48 unique columns of length 5
        f(5, 1) = 48
        f(1, 1) = 3
        f(1, 2) = 6
        f(2, 1) = 6
        f(2, 2) = 18
        f(2, 3) = 54
        f(2, 4) = 162
        f(4, 2) = 162
        The functions seems to be symmetric so both left-right and up-down adjacent is excluded 
        A bitmask for each color in a given column
        
        f(5, 1):
         R, G, B    Color
        [0, 0, 1]   [2]
        [0, 1, 0]   [1] 
        [0, 0, 1]   [2]
        [1, 0, 0]   [0]
        [0, 0, 1]   [2]
        Each cell needs to be colored -> there must be exactly one set bit in every row
        no adjacent same color ->  No two bits set in a row in a single column 
        Should be able to ecnode it orderly instead of one-hot 
        """

        states = get_valid_coloring(m)
        s = len(states)

        #BUild the transitions between states 
        edges = defaultdict(list)
        for i in range(s):
            for j in range(i+1, s):
                if can_transition(states[i], states[j]):
                    edges[i].append(j)
                    edges[j].append(i)
                
        dp = [[0] * s for _ in range(n)]
        #Init base case, any state can only be chosen in one way 
        for i in range(s):
            dp[0][i] = 1
            
            
        #Build dp array
        for col in range(1, n):
            for curr in range(s):
                for prev in edges[curr]:
                    dp[col][curr] = (dp[col][curr] + dp[col-1][prev]) % MOD
            
        # SUm the total number
        tot = 0
        for i in range(s):
            tot = (tot + dp[n-1][i]) % MOD
        return tot
    
        
# @lc code=end

