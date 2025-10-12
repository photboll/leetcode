#
# @lc app=leetcode id=3539 lang=python3
#
# [3539] Find Sum of Array Product of Magical Sequences
#

# @lc code=start
from math import comb
from functools import cache

from collections import defaultdict
MOD = pow(10, 9) + 7

class Solution:
    def magicalSum(self, total_count: int, bit_target: int, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dfs(remaining, bits_needed, index, carry):
            """
            remaining: How many numbers we still need to select 
            bits_needed: How many more bits need to be set for the sequence to become magical
            nums[index]: is the currently considred number. how many magical sequnces can it be a part of?
            carry: the current partial sum of the magical sequence 
            """
            if remaining < 0 or bits_needed < 0 or remaining + carry.bit_count() < bits_needed:
                return 0
            if remaining == 0 and bits_needed == carry.bit_count():
                #we have a sequnce of m numbers which are magical 
                return 1
            if remaining == 0:
                return 0
            if index >= n:
                return 0
            
            res = 0
            #We can use nums[index] multiple times, try for every possible number of repeats
            for repeated in range(remaining+1):
                #If we find a magical sequence we can permute it to create comb() other magical sequences
                #Comb(remaining, repeated)
                ways = comb(remaining, repeated) * pow(nums[index], repeated, MOD) % MOD
                new_carry = carry + repeated
                res += ways * dfs(remaining - repeated, bits_needed - (new_carry % 2), index +1, new_carry // 2)
                res %= MOD
            return res
        
        return dfs(total_count, bit_target, 0, 0)

class SolutionV1:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        """
        The crux seem to be how to now how many bits will be set in binary repr. for that sum.
        wait a minute,
        
        each term of power will contain exactly one set bit. Since the number is a power of two
        The bit that will be set is the seq[i] bit. This reduces the binary repr. condition
        since each seq[i] number must be unique for its bit to be set. No, wait that is wrong. 
        duplicates are allowed. 

        Duplicate set bits are simply added together and make the seq[i]+1 bit set instead. 
        need to reduce this further, cant go over every number in the sequnce each time we add or remove 
        a number to the sequence 
        
        Sequence -> does not have to be contigious. we have n take m number of possible sequences. Which is a lot.
        we do know that m can NOT be < samller than k. if m < k then the bin repr. can at most have m bit set, which is a contradiction 
        Most magical sequences will be clustered around m=k. But m > k can produce magical sequences if there are duplicates.

        Maybe we can pre-process nums to remove the duplicates. This will lead to problems when trying compute the product

        We need to get the array product -> it is not enough to know the count of magical sequences
        but we can compute it for one member of a class and then compute how many permutations of that class can be made 
        multinominal gives us how many permutations with possible dupblicate numbers
        
        One BIG mistake I made. I assumed that we only could use each number once. But repetitions are allowed 

        """
        n = len(nums)

        #dp[i][j][mask] is the state after choosing i numbers
        #State is
        # 0 <= i < m
        # 0 <= j <=i, j is the number of set bits from the partial binrep S of the i number
        #mask represents the "window" of lower-order bits from S that have not yet been fully processed
        dp = defaultdict(defaultdict(defaultdict(int)))


        
# @lc code=end

