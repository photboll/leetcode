#
# @lc app=leetcode id=3756 lang=python3
#
# [3756] Concatenate Non-Zero Digits and Multiply by Sum II
#

# @lc code=start
MOD = pow(10, 9) + 7

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        m = len(queries)

        pref_sum = [0] * (n+1)#the sum of all digits
        pref_val = [0] * (n+1)# holds the x that is created from 0 till i
        pref_count= [0] *(n+1)#how many non/zero digits have appeared till i-1 since we dont store 0
        powers = [1] * (n+1)
        for i in range(1, n+1):
            powers[i] = (powers[i-1] * 10) % MOD

        
        # precompute the prefix sum
        for i in range(n):
            d = int(s[i])

            pref_sum[i+1] = pref_sum[i] + d
            pref_count[i+1] = pref_count[i] + (1 if d !=0 else 0)

            if d == 0:
                pref_val[i+1] = pref_val[i]
            else:
                pref_val[i+1] = (pref_val[i] * 10 + d) % MOD
        
        result = [0] * m

        for i in range(m):
            l, r = queries[i]
            length = pref_count[r+1] - pref_count[l]
            start = pref_val[l]
            end = pref_val[r+1]
            x = (end - (start * powers[length]) % MOD + MOD) % MOD

            result[i] = (x *(pref_sum[r+1] - pref_sum[l])) % MOD
        return result

            



        
# @lc code=end

