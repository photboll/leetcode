#
# @lc app=leetcode id=1262 lang=python3
#
# [1262] Greatest Sum Divisible by Three
#

# @lc code=start


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        """
        if num % 3 == 0 then it will always belong to the greates sum
        if num % 3 == 1 we need an additional num % 3 == 2 to be added as well
        to keep the sum divisible by three  
        """
        def min2(a, b, c):
            """
            a must be >=b
            """
            if c < a:
                return c, a
            elif c < b:
                return a, c
            else:
                return a, b

        rem1 = (float("inf"), float("inf"))
        rem2 = (float("inf"), float("inf"))
        total = 0
        for num in nums:
            total += num
            rem = num % 3
            if rem == 1:
                rem1 = min2(*rem1, num)
            elif rem == 2:
                rem2 = min2(*rem2, num)

        tot_rem = total % 3
        #print(total, rem1, rem2)

        if tot_rem == 0:
            return total
        elif tot_rem == 1:
            # we can remove one from rem1 or two from rem2
            op1 = rem1[0]
            op2 = rem2[0] + rem2[1]
        else:
            #We can remove one from rem2 or two from rem1
            op1 = rem2[0]
            op2 = rem1[0] + rem1[1]

        return total - min(op1, op2)
            
            
        
# @lc code=end

