#
# @lc app=leetcode id=3343 lang=python3
#
# [3343] Count Number of Balanced Permutations
#

# @lc code=start
from collections import Counter
from functools import cache
MOD = pow(10, 9) + 7
class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        """
        since it is a hard problem it is presumably to slow to bruteforce it
        The order of num does not matter, only the frequency of each digit.
        ONly Count distinct permutations, so we need to reduce identical
        We have n positions and freqs of each digit.
        Which position a specifc digit is assigned to does not matter for it being balanced. 
        It only matters if the position is odd or even. 
        If we have an even number of positions then any balanced string will a symmetric string that is also balance
        "1221" and "2112"
        We want to partition num into two parts that differ atmost in length by 1
        both parts need to have the same sum, which means that the total sum of all digits must be even 
        Then we count the number of distinct permutations that can be made in each partition 
        """
        nums =  [int(i) for i in num]
        freqs = Counter(nums)
        #The total needs to e even or else we cant partitions the digits in two equal partitions
        tot_sum = sum(nums)
        if tot_sum % 2 == 1:
            return 0
        target = tot_sum // 2

        n = len(nums)
        max_odd = (n+1) // 2
        psum = [0] * 11
        for digit in range(9, -1,-1):
            psum[digit] = psum[digit+1] + freqs[digit]
            
        @cache
        def dfs(pos, curr, odd_count):
            if odd_count < 0 or psum[pos] < odd_count or curr > target:
                return 0
            
            if pos > 9:
                return int(curr == target and odd_count == 0)
            
            #Even positions left to fill 
            even_count = (psum[pos] - odd_count)
            res = 0
            for k in range(max(0, freqs[pos] - even_count), min(freqs[pos], odd_count) + 1):
                #Place k of the current number at od positions, and the remaining in the evencount
                ways = comb(odd_count, k) * comb(even_count, freqs[pos] - k) % MOD
                res += ways * dfs(pos + 1, curr+k*pos, odd_count - k)
            return res % MOD
        
        
        return dfs(0,0, max_odd)

        
# @lc code=end

