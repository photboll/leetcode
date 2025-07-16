#
# @lc app=leetcode id=3201 lang=python3
#
# [3201] Find the Maximum Length of Valid Subsequence I
#

# @lc code=start

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        """
        DP approach:
        The modulo two operation gives us wheter or not the sum of the terms is odd or even.
         
        The sequnce of equalities implies that a subsequnce sub can either have parity 0 or 1.
        They can both be valid but the parity must stay the same when extending sub.
        if subs parity is 1: then subs numbers will oscillate between 0 and 1
        if subs partiy is 0: then the numbers will be wither all even or all odd.
        in total a valid subsequnce can be of four types:
        1. parity is 1 and successive elements flip between being odd and even
        2. parity is 1 and successive elements flip between being even and odd 
        3. parity is 0 and all elements are even.
        4. parity is 1 and all elements are odd.

        if nums have length 2, then the answer is always two.
        
        let us consider the ith element of nums:
        if nums[i] is even then it can extend type 3 by one and it can be used to extend the best of type 1
        
        """
        #Pure subsquence where all numbers have the same parity
        even_even = 0
        odd_odd = 0
        
        #Alternating subsequences ending in an ODD number
        len_ends_odd = 0
        #longest alternating subsequence ending in an even number 
        len_ends_even = 0
        
        
        for num in nums:
            is_odd = num % 2
            
            #Extend the previous best "pure" subs
            if is_odd:
                odd_odd += 1
                #An odd number can extend an alternating sequence ending with an even number
                len_ends_even = len_ends_odd + 1
            else:
                even_even += 1
                #An even number can extend an alternating sequence ending with an odd number
                len_ends_odd = len_ends_even + 1
        
        return max(even_even, odd_odd, len_ends_even, len_ends_odd)
            
                

        
# @lc code=end

