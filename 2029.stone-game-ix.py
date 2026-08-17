#
# @lc app=leetcode id=2029 lang=python3
#
# [2029] Stone Game IX
#

# @lc code=start
class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        """
        divisble by 3, only the stones mod 3 will matter. one choosing stones that 
        is. they will still affect the total score. no wait the bob wins when all stones are picked
        makes it redundant 
        possible states 
        cur value:
        0: pick either 1 or 2. initial state 
        1: pick a stones mod 3 = 1 or mod 3 == 0
        2: pick stones mod 3 = 2 or mod 3 == 0

        what matters is how many stones mod 3 == 0. essentially a pass makes it the opponents turn
        stones mod 3 == 1
        """
        count0 = count1 = count2 = 0

        for num in stones:
            rem = num % 3 
            if rem == 0:
                count0 += 1
            elif rem == 1:
                count1 += 1
            else :
                count2 += 1

        #even number of turn switches
        if count0 % 2 == 0:
            return count1 >= 1 and count2 >= 1
        
        return count1 - count2 > 2 or count2 - count1 > 2
            


        
# @lc code=end

