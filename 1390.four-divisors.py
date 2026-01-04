#
# @lc app=leetcode id=1390 lang=python3
#
# [1390] Four Divisors
#

# @lc code=start

from functools import cache
from collections import defaultdict

def sieve(n):
    if n < 2:
        return []
    is_prime = [True] * (n//2+1)
    is_prime[0] = False

    for i in range(3, int(n ** 0.5) +1, 2):
        if is_prime[i //2]:
            for j in range(i*i, n+1, 2*i):
                is_prime[j//2] = False
    return [2] + [2*i + 1 for i in range(1, len(is_prime)) if is_prime[i]]

@cache
def prime_decomposition(n, primes):
    factors = {}
    for p in primes:
        if p * p > n:
            break
        while n% p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
    if n> 1:
        factors[n] = factors.get(n, 0) + 1
    return factors
        
    
        

class Solution:
    def __init__(self):
        self.divisors = {}
        self.primes = tuple(sieve(10**5))
        
    def sumFourDivisors(self, nums: List[int]) -> int:
        """
        nums[i] is capped at 100 000
        max 4 divisors implies that the prime decomposition of num
        can not have more than 2 entries (p, q). then we have the 4 divisors 
        [1, p, q, pq]
        we can also get 4 divisors if p == q
        [1, p, p*p, p*p*p]
        """
        result = 0
        for num in nums:
            #We may have already computed it for num
            if num in self.divisors:
                result += self.divisors[num]
                continue

            factors = prime_decomposition(num, self.primes)
            if len(factors) == 2:
                #p, q the only valid case
                p, q = factors.keys()
                if factors[p] == 1 and factors[q] == 1:
                    self.divisors[num] = 1 + p + q + p*q
                else:
                    self.divisors[num] = 0
                
            elif len(factors) == 1:
                p, = factors.keys()
                if factors[p] == 3:
                    self.divisors[num] = 1 + p + p*p + p*p*p
                else:
                    self.divisors[num] = 0
            else:
                #num have none-4 divisors, its contribution to the result will be 0
                self.divisors[num] = 0
            
            result += self.divisors[num]


        return result


        
# @lc code=end

