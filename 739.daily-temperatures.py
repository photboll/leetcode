#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        
        result = [0] * n
        mon_stack = []
        for i in range(n-1, -1,-1):
            temp = temperatures[i]

            while mon_stack and temp >= temperatures[mon_stack[-1]]:
                #Later values that are smaller then the current can't affect the answers
                mon_stack.pop()

            if not mon_stack:
                result[i] == 0
                mon_stack.append(i)
                continue
            result[i] = mon_stack[-1] - i 
            mon_stack.append(i)
        return result
            
            


            
        
# @lc code=end

