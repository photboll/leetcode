#
# @lc app=leetcode id=2336 lang=python3
#
# [2336] Smallest Number in Infinite Set
#

# @lc code=start
from heapq import heappush, heappop, heapify
class SmallestInfiniteSet:

    def __init__(self):
        self.heap = [i+1 for i in range(1000)]
        heapify(self.heap)
        self.used = [False] * 1000

    def popSmallest(self) -> int:
        val = heappop(self.heap)
        self.used[val-1] = True
        return val
    
    def addBack(self, num: int) -> None:
        if self.used[num-1]:
            heappush(self.heap, num)
            self.used[num-1] = False
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
# @lc code=end

