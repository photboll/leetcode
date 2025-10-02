#
# @lc app=leetcode id=3100 lang=python3
#
# [3100] Water Bottles II
#

# @lc code=start
from math import sqrt, ceil

class SolutionGreedy:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        empty = numBottles
        
        while empty >= numExchange:
            empty -= numExchange
            total += 1
            empty += 1
            numExchange += 1
        return total 


class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        def formula(numBottles, numExchange):
            res = ceil(-(2 * numExchange -3) + sqrt((2*numExchange - 3)**2 + 8 * numBottles))
        
        return numBottles + formula(numBottles, numExchange)

class SolutionV1:
    #this is wrong the formula is incorrect and the while loop should not be necessary with the formula
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        def formula(start, max_sum):
            res = -1 + sqrt(1 + 4 *(2*max_sum + (start-1)*start))
            return int(res) // 2

        total = 0
        
        while numBottles >= numExchange:
            #Drink all available full bottles
            print(numBottles, numExchange, total)
            total += numBottles
            numBottles = formula(numExchange, numBottles)
            numExchange += numBottles
        
        print(numBottles, numExchange, total)
        total += numBottles
        return total 
        
        
        
# @lc code=end

