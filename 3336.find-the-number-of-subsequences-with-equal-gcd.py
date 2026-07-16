#
# @lc app=leetcode id=3336 lang=python3
#
# [3336] Find the Number of Subsequences With Equal GCD
#

# @lc code=start
import math
MOD = pow(10, 9) + 7
class Solution:

    def subsequencePairCount(self, nums: List[int]) -> int:
        max_v = max(nums)

        mu = [0] * (max_v + 1)
        mu[1] = 1
        primes = []
        is_prime = [True] * (max_v + 1)

        for i in range(2, max_v + 1):
            if is_prime[i]:
                primes.append(i)
                mu[i] = -1
            
            for p in primes:
                if i * p > max_v: break
                is_prime[i*p] = False
                if i % p == 0:
                    mu[i*p] = False
                    break
                else:
                    mu[i*p] = -mu[i]
        
        # 2. Precompute Mobius coefficients: Coeff(M1, M2)
        coeff = [[0] * (max_v + 1) for _ in range(max_v + 1)]
        for g in range(1, max_v + 1):
            for m1 in range(g, max_v + 1, g):
                m1_mu = mu[m1 // g]
                if m1_mu == 0: continue
                for m2 in range(g, max_v + 1, g):
                    m2_mu = mu[m2 // g]
                    coeff[m1][m2] += m1_mu * m2_mu
        
        # 3. Precompute count of multiples for each value
        count_nums = [0] * (max_v + 1)
        for x in nums: count_nums[x] += 1
        count_mult = [0] * (max_v + 1)
        for g in range(1, max_v + 1):
            for x in range(g, max_v + 1, g):
                count_mult[g] += count_nums[x]
        
        # 4. Precompute powers of 2 and 3
        n = len(nums)
        pow2, pow3 = [1] * (2 * n + 1), [1] * (n + 1)
        for i in range(1, 2 * n + 1): pow2[i] = (pow2[i-1] * 2) % MOD
        for i in range(1, n + 1): pow3[i] = (pow3[i-1] * 3) % MOD
                
        # 5. Calculate total pairs using the Mobius inversion formula
        ans = 0
        for m1 in range(1, max_v + 1):
            ac = count_mult[m1]
            if ac == 0: continue
            for m2 in range(1, max_v + 1):
                bc = count_mult[m2]
                if bc == 0 or coeff[m1][m2] == 0: continue
                
                lcm_val = (m1 * m2) // math.gcd(m1, m2)
                c = count_mult[lcm_val] if lcm_val <= max_v else 0
                
                # F(M1, M2) calculation via inclusion-exclusion
                term = (pow3[c] * pow2[ac + bc - 2 * c]) % MOD
                term = (term - pow2[ac] - pow2[bc] + 1) % MOD
                ans = (ans + term * coeff[m1][m2]) % MOD
                    
        return ans % MOD    
            
        
# @lc code=end

