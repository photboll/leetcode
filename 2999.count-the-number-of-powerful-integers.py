#
# @lc app=leetcode id=2999 lang=python3
#
# [2999] Count the Number of Powerful Integers
#

# @lc code=start
def numberOfpowerfulIntLessThan(finish: int, limit: int, s:str) -> int:
    """
    We need to know what is the limiting factor of each possbile position.
    Is it the end of the interval finsih or is the limit?
    for each possible positoin X_i
    if finish[i] < limit then we have fewer choices for this position
    but how will the remaining choices be affected by this?
    I think it would affect all choices until we first encounter a position where limit is the limiting factor.
    we would also get a sort of "remainder" 
    
    """
    fin = str(finish)
    result = (finish <= int(s))#is the suffix itself in the range
    choices = 1
    msb_passed = False
    for i in range(len(fin)- len(s)):
        print(i, fin[i], limit)
    
    return result

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        """
        The main idea is to start with the suffix and then prepend all available digits (those at mort equal to  limit )
        We need to be mindful of which are within and outside the interval 
        start with simplifying the interval, lets say start=1 and finish=99999
        for suffix = "53" all powerful integers must have the following form
        "XXX53" Where each X is a digit from [0,..., limit] so the answer will be 
        (limit+1)**3
        it is simply the number of ways we can choose each digit
        Now we need to know how to get all powerful integers less than finish.
        When we know that we can simply compute powerful ints lt finish - powerful ints lt start to get the answer
        
        """
    
        return numberOfpowerfulIntLessThan(finish, limit, s) - numberOfpowerfulIntLessThan(start, limit, s)
# @lc code=end

