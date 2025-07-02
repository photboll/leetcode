#
# @lc app=leetcode id=3333 lang=python3
#
# [3333] Find the Original Typed String II
#

# @lc code=start
import collections

MOD = 10**9 + 7

class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        """
        Calculates the number of possible original strings of length at least k.

        This solution uses the principle of inclusion-exclusion (complement counting)
        combined with generating functions for an efficient O(k^2) calculation.

        1.  The total number of strings without a length constraint is the product
            of the lengths of consecutive identical character groups.
        2.  We calculate the number of "invalid" strings (length < k) and subtract
            this from the total.
        3.  The count of strings of a specific length is modeled using generating
            functions. The number of ways to form a string of length L is the
            coefficient of x^L in a complex polynomial product.
        4.  We use advanced techniques (logarithmic derivative and convolution with
            prefix sums) to efficiently calculate the sum of coefficients for
            lengths less than k.
        """
        if not word:
            return 0

        # 1. Pre-process word: find lengths of consecutive character groups
        # and their frequencies.
        counts = []
        i = 0
        n = len(word)
        while i < n:
            j = i
            while j < n and word[j] == word[i]:
                j += 1
            counts.append(j - i)
            i = j

        freq_map = collections.Counter(counts)
        m = len(counts)  # Total number of character groups

        # 2. Calculate the total number of possible original strings (ignoring length)
        total_ways = 1
        for c in counts:
            total_ways = (total_ways * c) % MOD

        # 3. Handle the edge case where the minimum possible length (m) is already >= k.
        # In this case, all possible strings are valid.
        if k <= m:
            return total_ways

        # 4. Calculate the complement: number of strings with length < k.
        # This is equivalent to sum of ways for length L, where m <= L < k.

        # Let P(x) be the generating function. The number of ways for length L is [x^L]P(x).
        # P(x) = product(x + x^2 + ... + x^c) = x^m * (1-x)^(-m) * B(x)
        # where B(x) = product(1 - x^c).
        # We need sum_{L=m..k-1} [x^L]P(x) = sum_{j=0..k-1-m} [x^j]((1-x)^(-m) * B(x)).
        
        # 4a. Compute coefficients of B(x) using the log-derivative trick.
        # First, find coefficients g_d of G(x) = (log B(x))'.
        g = [0] * k
        for c, p in freq_map.items():
            val = (p * c)
            # G(x) = sum -p*c * (x^(c-1) + x^(2c-1) + ...)
            for j in range(c, k, c):
                g[j - 1] = (g[j - 1] - val) % MOD
        
        # Second, find coefficients b_d of B(x) using the recurrence:
        # d*b_d = sum_{i=0..d-1} g_i * b_{d-1-i}
        b = [0] * k
        b[0] = 1
        
        # Precompute modular inverses needed for the division by d.
        inv = [0] * k
        if k > 1:
            inv[1] = 1
        for i in range(2, k):
            inv[i] = MOD - (MOD // i) * inv[MOD % i] % MOD

        for d in range(1, k):
            # This is a convolution: sum_{i=0..d-1} g_i * b_{d-1-i}
            sum_val = 0
            for i in range(d):
                term = (g[i] * b[d - 1 - i]) % MOD
                sum_val = (sum_val + term) % MOD
            b[d] = (sum_val * inv[d]) % MOD
            
        # 4b. Compute prefix sums of b (S_B).
        S_B = [0] * k
        S_B[0] = b[0]
        for i in range(1, k):
            S_B[i] = (S_B[i - 1] + b[i]) % MOD
            
        # 4c. Combine coefficients of B(x) and (1-x)^(-m) to get the final count.
        # The sum is efficiently calculated as: sum_{i=0..J} a_i * S_B(J-i)
        # where J = k-1-m and a_i are coefficients of (1-x)^(-m).
        ways_less_than_k = 0
        J = k - 1 - m
        
        if J >= 0:
            # a_i = C(m+i-1, i). We compute a_i iteratively.
            a_i = 1  # a_0 = C(m-1, m-1) = 1
            
            for i in range(J + 1):
                term = (a_i * S_B[J - i]) % MOD
                ways_less_than_k = (ways_less_than_k + term) % MOD
                
                # Update a_i to a_{i+1} using: a_{i+1} = a_i * (m+i) / (i+1)
                term1 = (m + i)
                term2 = inv[i + 1]
                a_i = (a_i * term1) % MOD
                a_i = (a_i * term2) % MOD
        
        # 5. Final Result: Total ways - complement
        return (total_ways - ways_less_than_k + MOD) % MOD

class SolutionEDIT:
    def possibleStringCount(self, word: str, k: int) -> int:
        """
        All possible intended strings will have a length of at least k and at most len(word) = n
        Would it help to repeatedly count all possible strings of each length?
        in a sequnce of repeated chars of sequnce m there will be m-1 different ways to delete them. The total number of possible strings
        will be the cumulative product of m-1 for each such sequence. How do we check that how many of them are atleast of length k?
        "aabbbcccccddddd" transform it to the list of repeated chars -1 (we know that there must be atleast on occurence of this char)
        [1, 2, 3, 4] the sum of this list need to be atleast k. The product of this list gives the total number of possible original strings.
        
        When k = 0 any combination of deleted chars is allowed. is this a subsolution of the case for k+1?
        
        Is it easier to calculate the complement? number of string of at most k-1.
         
        """
        n  = len(word)
        #compute the run length frequencies 
        count = 1
        freqs = []
        
        for i in range(1, n):
            if word[i] != word[i-1]:
                freqs.append(count)
                count = 1
            else:
                count += 1
        freqs.append(count)
        
        #Compute the cumulative product modulo MOD
        res = 1
        for f in freqs:
            res =  (res * f) % MOD
        
        #Each group of chars need to have atleast one intended char, else would never have pressed the key
        #if k is smaller then the number of groups, all strings will be at least of length k
        if len(freqs) >= k:
            return res

        
        #the base case with prefix sum optimization 
        f = [1] + [0] * (k -1)
        g = [1] * k
        
        for i in range(len(freqs)):
            f_new = [0] * k
            for j in range(1, k):
                f_new[j] = g[j-1]
                if j - freqs[i] - 1>= 0:
                    f_new[j] = (f_new[j] - g[j-freqs[i] -1]) % MOD
                
                g_new = [f_new[0]] + [0] * (k-1)
                for j in range(1, k):
                    g_new[j] = (g_new[j-1] + f_new[j]) % MOD
                
            f = f_new
            g = g_new
                
        
        return (res - g[k-1]) % MOD
# @lc code=end

