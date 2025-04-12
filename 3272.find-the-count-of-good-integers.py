#
# @lc app=leetcode id=3272 lang=python3
#
# [3272] Find the Count of Good Integers
#

# @lc code=start
from collections import Counter
from math import factorial
def get_palindromic_nums_count_of_length_n(n: int) -> int:
    if n == 1:
        #Any single digit number is a palindrome
        return 10
    result  = 9#The first digit must be in [1, 9]
    #We can choose the ramining first half of the numbers digits freely from [0, 9]
    for _ in range(1, n//2):
        result *= 10
        
    #odd length numbers also have a middle digit that can be chosen 
    if n % 2 == 1:
        result*= 10
    return result

def get_palindromic_nums_of_length(n:int) -> List[int]:
    results = []
    digits = [""]*n
    
    def backtrack(i):
        if 2 * i >= n:  
            results.append(int("".join(digits)))
            return

        for digit in map(str, range(10)):
            if i == 0 and digit == "0":
                #leading zeros are not allowed
                continue
            
            digits[i] = digit
            digits[n-1-i] = digit
            backtrack(i+1)
            #No need to remove them, since they get overwritten in the next iteration
        
    backtrack(0)
    return results

def get_k_palindromic_nums_of_length(n:int, k:int) -> List[int]:
    palindromes = get_palindromic_nums_of_length(n)
    result = []
    for num in palindromes:
        if num % k == 0:
            result.append(num)
    return result
    
def get_unique_digit_freqs(nums):
    unique_digit_freqs = set()
    for num in nums:
        fset = get_ordered_digit_freqs(num)
        unique_digit_freqs.add(fset)
        
    return unique_digit_freqs

def get_ordered_digit_freqs(num):
    freqs = Counter()
    while num > 0:
        num, digit = divmod(num, 10)
        freqs[digit] += 1
    return frozenset(freqs.items())

def count_permutations(n, freqs):
    """
    computes the multinomial 
    sum of all freqs need to be n
    """
    valid_permutations = factorial(n)
    for _, freq in freqs:
        valid_permutations//= factorial(freq)

    return valid_permutations  
    
class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        """
        we only care about numbers with a fixed amount of digits, at each call
        Do we need to find all k-palindromic integers or can we calculate how many there will be?
        Checking the divisible constraint might be difficult with out creating them 
        maybe it is possbile to do it in two steps.
        1. filter out all numbers which are not palindromes
        2. filter out the numbers which are not divisble by k
        3. The numbers remaining should be k palindromic
        4. all permutations of these number will be good, first position will have to be larger than 0 
        the upper onstraint is 10 digit numbers, intuitevly it seems to hint that we can't create every single number and check
        them. but it might still be possible to brute-force it if we have a good pruning strategy
        To find all k-palindromes. First find all palindromes with n digits
        We only have a free choice on the first half of the digits, since the palindrome constraint forces the second half to be the reverse
        The first postion must be larger than 0 or else we will get leading zeros, which was not allowed
        the remaining positions can be chosen from [0, 9]        
        """
        k_palindromes = get_k_palindromic_nums_of_length(n, k)
        #Convert k_palindromes into a set of frequency counts of each digit
        #To prevent overcounting.
        #The rearrangment of a k_palindrome into a good integer will otherwise double count 
        #The same good integer, since we can arrive at it from two different k_palindromes.
        unique_digit_freqs = get_unique_digit_freqs(k_palindromes)
        #each set of digit freqs can now be arranged to every single good integer
        #Keep in mind that zeros are not allowed to lead
        total = 0
        for freqs in unique_digit_freqs:
            ordered_freqs = sorted(list(freqs))
            num_permutations = count_permutations(n, ordered_freqs)
            #Any number that contains at least one zero, will create permutations which start with a leading zero
            if ordered_freqs[0][0] == 0:
                #Remove all arrangements which start with a leading zero
                ordered_freqs[0] = (0, ordered_freqs[0][1] -1)
                num_permutations -= count_permutations(n-1, ordered_freqs)
                 
            total += num_permutations
        return total
        

        

        
# @lc code=end

