#
# @lc app=leetcode id=901 lang=python3
#
# [901] Online Stock Span
#

# @lc code=start
class StockSpanner:

    def __init__(self):
        self.stack = []# (price, span)
        

    def next(self, price: int) -> int:
        #There was no previous price  
        if len(self.stack) == 0 or self.stack[-1][0] > price: 
            self.stack.append((price, 1))
            return 1
        
        #We know that self.stack[-1] <= price
        curr_span = 1 #Including today
        while self.stack and self.stack[-1][0] <= price:
            _, span = self.stack.pop()
            curr_span += span
        
        self.stack.append((price, curr_span))
        return curr_span
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end

