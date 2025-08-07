#
# @lc app=leetcode id=3363 lang=python3
#
# [3363] Find the Maximum Number of Fruits Collected
#

# @lc code=start
class Solution:
    def maxCollectedFruits(self, fruits):
        n = len(fruits)
        ans = sum(fruits[i][i] for i in range(n))

        def dp():
            prev = [float("-inf")] * n
            curr = [float("-inf")] * n
            prev[n - 1] = fruits[0][n - 1]
            for i in range(1, n - 1):
                for j in range(max(n - 1 - i, i + 1), n):
                    best = prev[j]
                    if j - 1 >= 0:
                        best = max(best, prev[j - 1])
                    if j + 1 < n:
                        best = max(best, prev[j + 1])
                    curr[j] = best + fruits[i][j]
                prev, curr = curr, prev
            return prev[n - 1]

        ans += dp()

        for i in range(n):
            for j in range(i):
                fruits[i][j], fruits[j][i] = fruits[j][i], fruits[i][j]

        ans += dp()
        return ans

class SolutionTLE:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        """
        Base case: 2x2 grid. Everyone gets 1 move. The entire grid of fruits gets collected. 
        We have a total of n-1 time steps and a total of 9 possible choices to make.
        Each child need to move in one of the 3 possible ways. 3x3 = 9 total choices. THIs is incoorect 
        Maybe it would be easier to model it from the opposite way, all children starting at n-1 and moving to their own goal
        
        Child 0 is actually forced to take the diagonal path to the goal. Since that is the only way they can make it to (n-1, n-1) in n-1 steps
        Child 1 and 2 won't intersect the diagonal, since moving past the diagonal will make it impossible to arrive at the goal in time.
        This means that in each time step the effective grid will reduce in size by one. 
        
        in Total we have:
        Child 0s i and j-coord will always be the same as the current time.
        Child 1s i-coord will always be the same as the current time.
        child 2s j-coord will always be the same as the current time.
        Together any valid stat can be described by the tuple (time, Child1j, child2i)
        And the possible transitions are to (time+1, child1j +- 1, child2i +- 1 )
        For a total of 6 different transitions.
        Some of which are usually invalid since j1 < time and i2 > time since they can#t cross the diagonal.
        """
        
        n = len(fruits)
        memo = {}

        def dp(time, j1, i2): 
            # Base case 1: when time reaches n, the game is over and no more fruits will be collected
            if time == n:
                return 0
            
            # Base Case 2: Check for an invalid state
            #Check if the current state is valid i.e. child 1 is above and child 2 is below the diagonal
            # And both are within bounds of fruits
            if not (0 <= j1 < n and 0 <= i2 < n and j1 >= time and i2 >= time):
                return float("-inf")
            
            if (time, j1, i2) in memo:
                return memo[(time, j1, i2)]
            
            fruit_count = fruits[time][time]# CHild 0s fruits
            if j1 != time:
                fruit_count += fruits[time][j1]# Child 1
            if i2 != time:
                fruit_count += fruits[i2][time]
            
            max_future_fruits = float("-inf") # means invalid 
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    #Find the maximum possible fruit count that can be reached from this state
                    max_future_fruits = max(dp(time+1, j1+dj, i2+di), max_future_fruits)
        
            memo[(time, j1, i2)] = fruit_count + max_future_fruits
            return memo[(time, j1, i2)]
        return dp(0, n-1, n-1)
                
            
        
# @lc code=end

