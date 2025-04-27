#
# @lc app=leetcode id=2462 lang=python3
#
# [2462] Total Cost to Hire K Workers
#

# @lc code=start
from heapq import heappush, heappop
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        heap = []
        n = len(costs)
        left = 0
        right = n-1
        
        
        
        for _ in range(candidates):
            if left<= right:
                heappush(heap, (costs[left], left, True))#(cost of hiring left, index, is_left)
                left += 1
            if left <= right:
                heappush(heap, (costs[right], right, False))
                right -= 1
        
        total_cost = 0
        while k > 0:
            print(k, left, right, len(heap), n, print(heap))
            cost, _, is_left = heappop(heap)
            total_cost += cost
            k -= 1

        
            if left <= right:
                if is_left:
                    heappush(heap, (costs[left], left, True))
                    left+= 1
                else:
                    heappush(heap, (costs[right], right, False))
                    right -= 1

        return total_cost
        
# @lc code=end

