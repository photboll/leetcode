#
# @lc app=leetcode id=3013 lang=python3
#
# [3013] Divide an Array Into Subarrays With Minimum Cost II
#

# @lc code=start
from bisect import bisect_left
from sortedcontainers import SortedList

class SmartWindow:
    def __init__(self, k):
        self.K = k
        self.low = SortedList()
        self.high = SortedList()
        self.sum_low = 0

    def window_size(self):
        return len(self.low) + len(self.high)
    
    def _erase_one(self, arr, x):
        i = bisect_left(arr, x)
        if i < len(arr) and arr[i] == x:
            arr.pop(i)
            return True
        return False
    
    def rebalance(self):
        need = min(self.K, self.window_size())

        while len(self.low) > need:
            #remove the largest in low
            x = self.low.pop() 
            self.sum_low -= x
            self.high.add(x)
        
        while len(self.low) < need and self.high:
            #remove the smallest in high
            x = self.high.pop(0)
            self.low.add(x)
            self.sum_low += x
    
    def add(self, x):
        if not self.low or x <= self.low[-1]:
            self.low.add(x)
            self.sum_low += x
        else:
            self.high.add(x)
        self.rebalance()
    
    def remove(self, x):
        if self._erase_one(self.low, x):
            self.sum_low -= x
        else:
            self._erase_one(self.high, x)
        self.rebalance()
    
    def query(self):
        return self.sum_low


class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        k -= 1
        window = SmartWindow(k)

        for i in range(1, 1+ dist+1):
            window.add(nums[i])
        
        result = window.query()

        for i in range(2, n-dist):
            window.remove(nums[i-1])
            window.add(nums[i+dist])
            result = min(result, window.query())

        return result + nums[0]
        
# @lc code=end

