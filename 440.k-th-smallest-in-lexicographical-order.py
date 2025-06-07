#
# @lc app=leetcode id=440 lang=python3
#
# [440] K-th Smallest in Lexicographical Order
#

# @lc code=start
class SolutionBrute:
    def findKthNumber(self, n, k):
        return int(sorted(list(map(str, range(1, n+1))))[k-1])
    
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        """
        lets start wiht answering, given n how many integers begin with a 1
        0 < n < 10 : 1 integer begins with 1
        9 < n < 20 : (n - 10) every int starts wiht a 1
        20 < n < 100: 0 no int starts with a 1
        99 < n < 200: (n - 100) every int start with a 1
        200 < n < 1000: 0
        
        0 < n < 10 : 1
        0 < n < 20 : 1 + (n - 10)
        0 < n < 100: 1 + 10 
        0 < n < 200: 1 + 10 + (n-100)
        0 < n < 1000: 1 + 10 + 100 
        
        Suppose we want to find how many integers start with "1" for a given n:
        n = 130_432
        every number in the span [100_000, 130_432] which is 30_432
        10_000 in the span [10_000, 99_999]
        1_000 in the span [1_000, 9_999]
        100
        10
        1
        The answer will be 11_111 + (30_432)
        
        Now we need to extend this logic for every digit 
        
        how many integers start with a 2 for n=130_432:
        in the span [1, 99_999] we have 11_111 integers starting with a 2
        in the span [100_000, 130_432] we have 0 integer starting with a 2, since they all start with 1
        The logic will be the same for all remaining digits
        
        with n = 130_432 and a given k. the first 41_543 digits start with a 1. 
        [1, 41_543] the kth smallest digits starts with a 1
        [41_544, 52_655] starts with a 2
        
        can we use this logic to recursively break down k until we are left with a string of digits? i think so
        The absolute first digit needs to be handled separetly
        
        suppose k = 33_123 then the first digits is 1 how should we procced?
        we are back to a similar question as we started. How many digits in [1, 130_432]
        starting with 1 have the second digit as 0?
        10, [100, 109], [1000, 1099], [10_000, 10_999], [100_000, 109_999]
        1 + 10         +100         + 1000             + 10_000
        11_111 integers start with 10
        11_111 integers start with 11
        and so on .
        33_123 // 11_111 = 2
        so the 33_123th number should start with 12. 33_123 - 22_222 = 10901
        What will be the third digit 
        120, [1200, 1209], [12_000, 12_099], [120_000, 120,999]
        1 + 10 + 100 + 1000 = 1111
        10901 // 1111 = 9
        the third digit should be 9, 10_901 - 9 * 1_111 = 902
        129x, [12_9x0, 12_9x9], [129_x00, 129_x99]
        1 + 10 + 100
        902 // 111 = 8 fourth digit should be 8, 902- 8*111 = 14
        12_98x, [129_8x0, 129_8x9]
        1 + 10
        14 // 11 = 1 fifth digit shuld be 1, 14 - 11 = 3
        3 // 1 = 3 sixth digits should be 3, 
        129_813
        
        THis is wrong. the brute force soultion gives 129_808

        129_8xx is where my soltio deviates form the corrct one
        12_980, [129_800, 129_809]
        1+ 10
        """
        
        def count_steps(n, prefix1, prefix2):
            steps = 0
            while prefix1 <= n:
                steps += min(n+1, prefix2) - prefix1
                prefix1 *= 10
                prefix2 *= 10
            return steps
        
        
        curr = 1
        k -= 1
        while k > 0:
            step = count_steps(n, curr, curr+1)
            #step is too small for k, we nrrf to invrement the current digit
            if step <= k:
                curr += 1
                k -= step
            else:
                curr *= 10
                k -= 1
                
        return curr
        
# @lc code=end

