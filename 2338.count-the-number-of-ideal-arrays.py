#
# @lc app=leetcode id=2338 lang=python3
#
# [2338] Count the Number of Ideal Arrays
#
# https://leetcode.com/problems/count-the-number-of-ideal-arrays/description/
#
# algorithms
# Hard (27.41%)
# Likes:    657
# Dislikes: 71
# Total Accepted:    28.8K
# Total Submissions: 60.9K
# Testcase Example:  '2\n5'
#
# You are given two integers n and maxValue, which are used to describe an
# ideal array.
# 
# A 0-indexed integer array arr of length n is considered ideal if the
# following conditions hold:
# 
# 
# Every arr[i] is a value from 1 to maxValue, for 0 <= i < n.
# Every arr[i] is divisible by arr[i - 1], for 0 < i < n.
# 
# 
# Return the number of distinct ideal arrays of length n. Since the answer may
# be very large, return it modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: n = 2, maxValue = 5
# Output: 10
# Explanation: The following are the possible ideal arrays:
# - Arrays starting with the value 1 (5 arrays): [1,1], [1,2], [1,3], [1,4],
# [1,5]
# - Arrays starting with the value 2 (2 arrays): [2,2], [2,4]
# - Arrays starting with the value 3 (1 array): [3,3]
# - Arrays starting with the value 4 (1 array): [4,4]
# - Arrays starting with the value 5 (1 array): [5,5]
# There are a total of 5 + 2 + 1 + 1 + 1 = 10 distinct ideal arrays.
# 
# 
# Example 2:
# 
# 
# Input: n = 5, maxValue = 3
# Output: 11
# Explanation: The following are the possible ideal arrays:
# - Arrays starting with the value 1 (9 arrays): 
# ⁠  - With no other distinct values (1 array): [1,1,1,1,1] 
# ⁠  - With 2^nd distinct value 2 (4 arrays): [1,1,1,1,2], [1,1,1,2,2],
# [1,1,2,2,2], [1,2,2,2,2]
# ⁠  - With 2^nd distinct value 3 (4 arrays): [1,1,1,1,3], [1,1,1,3,3],
# [1,1,3,3,3], [1,3,3,3,3]
# - Arrays starting with the value 2 (1 array): [2,2,2,2,2]
# - Arrays starting with the value 3 (1 array): [3,3,3,3,3]
# There are a total of 9 + 1 + 1 = 11 distinct ideal arrays.
# 
# 
# 
# Constraints:
# 
# 
# 2 <= n <= 10^4
# 1 <= maxValue <= 10^4
# 
# 
# n = 2, maxValue = 7
# starting with 1, count=7 : [1, 1], [1, 2], [1, 3], [1, 4], [1,5], [1,6], [1, 7]
# starting with 2, count=3 : [2, 2], [2,4], [2,6]
# Starting with 3, count=2 : [3, 3], [3,6]
# Starting with 4, count=1 : [4, 4]
# Starting with 5, count=1 : [5, 5]
# Starting with 6, count=1 : [6, 6]
# Starting with 7, count=1 : [7, 7]
# Total count = 16

# n = 3, maxValue = 5
# Starting with 1, count=5 : [1,1,1],[1,1,2], [1,1,3],[1,1,4],[1,1,5] 
#Starting with 1,2 count=2 : [1,2,2],[1,2,4]
#STarting with 1,3 count=1 : [1,3,3]
#Starting with 1,4 count=1 : [1,4,4]
#Starting with 1,5 count=1 : [1,5,5]
# Starting with 2, count=2 : [2,2,2],[2,2,4],
#                        1 : [2,4,4]
# Starting with 3, count=1 : [3,3,3]
# Starting with 4, count=1 : [4,4,4]
# Starting with 5, count=1 : [5,5,5]
#Total count = 16



# @lc code=start
def idealArraysBT(n, maxValue):
    results = []
    arr = [1] * n
     
    def backtrack(i):
        if i == n:
            results.append(list(arr))
            return
        if i == 0:
            for k in range(1, maxValue+1):
                arr[0] = k
                backtrack(i+1)
            return 
        K = maxValue
        if i > 0:
            K //= arr[i-1]
           
        for k in range(1, K+1):
            arr[i] = arr[i-1] * k
            backtrack(i+1)
            
    backtrack(0)
    return results
MOD = pow(10, 9) + 7
MAX_N = pow(10, 4) + 10
MAX_P = 15 #At most 15 prime factors 

sieve = [0] * MAX_N
for i in range(2, MAX_N):
    if sieve[i] == 0:
        for j in range(i, MAX_N, i):
            sieve[j] = i

ps = [[] for _ in range(MAX_N)]
for i in range(2, MAX_N):
    x = i
    while x > 1:
        p = sieve[x]
        cnt = 0
        while x % p == 0:
            x //= p
            cnt += 1
        ps[i].append(cnt)
c = [[0]*(MAX_P + 1) for _ in range(MAX_N + MAX_P)]

c[0][0] = 1
for i in range(1, MAX_N + MAX_P):
    c[i][0] = 1
    for j in range(1, min(i, MAX_P) + 1):
        c[i][j] = (c[i-1][j] + c[i-1][j-1]) % MOD

class Solution:
    def idealArrays(self, n, maxValue):
        result = 0
        for x in range(1, maxValue+1):
            mul = 1
            for p in ps[x]:
                mul = mul * c[n+p-1][p] % MOD
            
            result = (result + mul) % MOD
        return result
class SolutionV1:
    def idealArrays(self, n: int, maxValue: int) -> int:
        #DP approach, we will find the solution for each n upto N.
        #The base case is when N = 1. Then the answer is the same as maxValue
        #the divisbility criterium aforces us to build each succesive solution by muliplying arr[i-1] * k while arr[i-1] * k <= maxValue
        #Which gives us K =  maxValue // arr[i-1], where each k can be in any integer in the interval [1, K]. This will guarantee that arr[i-1] * k <= max_value
        #Okay, i am stuck with this approach,
        #Maybe it is easier to set the last value of a array in range [1, maxValue]
        #if the last value is prime then it must be preceeded by 1 or it self
        
        dp = [1] * n
        dp[0] *= maxValue


        for i in range(1,n): 
            dp[i] *= dp[i-1] * (maxValue //  (i))
        print(dp)
        return dp[-1]
# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    inputs = [(2, 5), (4, 5), (3, 5), (2, 7), (5, 3), (3, 25), (7,7)]
    for n, maxValue in inputs:
        result2 = sol.idealArrays(n, maxValue)
        #print(f"{result=}")
        result = idealArraysBT(n, maxValue)
        print(result)
        print(len(result), result2)
        

