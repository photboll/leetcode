#
# @lc app=leetcode id=2197 lang=python3
#
# [2197] Replace Non-Coprime Numbers in Array
#

# @lc code=start
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        #Euclid's algorithm 
        def gcd(a, b):
            while b != 0:
                tmp = b
                b = a % b
                a = tmp

            return a
        

        stack = []
        for num in nums:
            while stack:
                a, b = num, stack[-1]
                com_denom = gcd(a, b)
                if com_denom == 1:
                    break
                stack.pop()
                num = a * (b // com_denom)

                #print(a, b, com_denom, stack)

            stack.append(num)
        
        return stack 
        
# @lc code=end

