#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#

# @lc code=start

from functools import cache

@cache
def factorial(n):
    return n * factorial(n-1) if n else 1
def getOrder(n, k):
    result = []
    while n> 1:
        n -= 1
        spanIndex, k = divmod(k, factorial(n))
        #print(n, k, factorial(n), spanIndex)
        result.append(spanIndex)
    result.append(0)#There should only be a single choice left at the end 
    return result

def orderToDigitSequence(order, digits="123456789"):
    available = [True] * (len(order) +1)
    result = ""
    
    for skipAvailable in order:
        count = -1
        for i in range(len(available)):
            if available[i]:
                count += 1
            if count == skipAvailable:
                result+= digits[i]
                available[i] = False                
                break
    return result
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        #The first digit can be chosen in n ways.
        #If we choose the first available digit then we will be in the ordered span [1, (n-1)![
        #If we choose the second available then we will be in the ordered span [(n-1)!, 2*(n-1)![
        #if we choose the third available then we will be in the ordered span [2*(n-1)!, 3*(n-1)![
        #We can do this in reverse. using n and k. The problem then becomes very similar to base changing of integers
        order = getOrder(n, k-1)
        
        return orderToDigitSequence(order)
# @lc code=end

