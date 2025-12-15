#
# @lc app=leetcode id=2110 lang=python3
#
# [2110] Number of Smooth Descent Periods of a Stock
#

# @lc code=start
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        stack =[prices[0]]

        def cumsum(k):
            return k * (k-1) // 2

        result = 0
        for i in range(1, n):
            p = prices[i]

            if p == stack[-1] -1:
                stack.append(p)
            else:
                #print(result, stack)
                
                result += cumsum(len(stack)+1)
                stack.clear()
                stack.append(p)

        result += cumsum(len(stack)+1)
        return result 
                
        
# @lc code=end

