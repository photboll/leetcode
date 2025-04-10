#
# @lc app=leetcode id=2999 lang=python3
#
# [2999] Count the Number of Powerful Integers
#

# @lc code=start

class Solution:
    def numberOfPowerfulInt(self, start, finish, limit, s):
        def noramlize(N):
            ans = 0
            less = False #Wheter the converted number is less than N
            for n in map(int, str(N)):
                if less:
                    ans = ans * 10 + limit
                elif n > limit:
                    less = True
                    ans = ans * 10 + limit
                else:
                    ans = ans * 10 + n
            return ans
        
        def count(N):
            ans = 0
            base = limit + 1
            prefix = str(N)[:-len(s)]
            for n in prefix:
                ans = ans * base + int(n)
            if int(prefix + s) <= N:
                ans += 1
            return ans

        return count(noramlize(finish)) - count(noramlize(start-1))

def numberOfpowerfulIntLessThan(finish: int, limit: int, s:str) -> int:
    """
    We need to know what is the limiting factor of each possbile position.
    Is it the end of the interval finsih or is the limit?
    for each possible positoin X_i
    if finish[i] < limit then we have fewer choices for this position
    but how will the remaining choices be affected by this?
    I think it would affect all choices until we first encounter a position where limit is the limiting factor.
    we would also get a sort of "remainder" 
    
    """
    fin = str(finish)
    n = len(fin)
    suffixLen = len(s)
    prefixLen = n - suffixLen
    if prefixLen < 0:
        return 0 #Suffix won't fit 
    dp = [[0,0] for _ in range(prefixLen+ 1)]#dp[i][tight]
    dp[0][1] = 1 #The empty prefix is tight with fin 
    for i in range(prefixLen):
        for tight in [0, 1]:
            max_digit = int(fin[i]) if tight else limit
            for d in range(0, min(max_digit, limit)+1):
                next_tight = tight and (d == max_digit)
                dp[i+1][next_tight] += dp[i][tight]
    
    total = dp[prefixLen][0] + dp[prefixLen][1]
    #check if the final number is actually inside the interval
    #Only one tight prefix path exists and we overshot the finish line
    if dp[prefixLen][1] == 1 and int(fin[:prefixLen] + s) > finish:
        total -= 1
        
    return total

class SolutionV1:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        """
        The main idea is to start with the suffix and then prepend all available digits (those at mort equal to  limit )
        We need to be mindful of which are within and outside the interval 
        start with simplifying the interval, lets say start=1 and finish=99999
        for suffix = "53" all powerful integers must have the following form
        "XXX53" Where each X is a digit from [0,..., limit] so the answer will be 
        (limit+1)**3
        it is simply the number of ways we can choose each digit
        Now we need to know how to get all powerful integers less than finish.
        When we know that we can simply compute powerful ints lt finish - powerful ints lt start to get the answer
        
        """
    
        return numberOfpowerfulIntLessThan(finish, limit, s) - numberOfpowerfulIntLessThan(start, limit, s)
# @lc code=end

