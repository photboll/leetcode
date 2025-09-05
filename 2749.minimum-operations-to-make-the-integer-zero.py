#
# @lc app=leetcode id=2749 lang=python3
#
# [2749] Minimum Operations to Make the Integer Zero
#

# @lc code=start
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        """
        We will atleast need a similar amount of operations as there are 1s in the binary representation
        of num1.
        num2 is constant regardless of how i is chosen. But we dont know ahead of time how many num2 will be subtracted
        We only have 61 choices for i at each step.
        Would it ever be desirable to choose the same i multiple times?
        """
        count = 1
        while True:
            x = num1 - num2*count
            if x < count:
                return -1
            if count >= x.bit_count():
                return count
            count += 1
    

        
# @lc code=end

