#
# @lc app=leetcode id=2761 lang=python3
#
# [2761] Prime Pairs With Target Sum
#

# @lc code=start
def get_(n):
    if n < 2:
        return 0
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    i = 2
    primes = []
    while i < n:
        if sieve[i]:
            primes.append(i)
            for j in range(i*i, n, i):
                sieve[j] = False
            
        i += 1
    return primes
class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        prime = [True] * (n+1)
        prime[0] = prime[1] = False
        result = []
        p = 2

        while p * p <= n:
            if prime[p]:
                for i in range(p*p, n+1,p):
                    prime[i] = False
            p += 1

        for i in range(2, n):
            if prime[i] and prime[n-i] and i <= n-i:
                result.append([i, n-i])

        return result
                

        

        
# @lc code=end

