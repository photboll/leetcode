#
# @lc app=leetcode id=1331 lang=python3
#
# [1331] Rank Transform of an Array
#

# @lc code=start
from heapq import heapify, heappop
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n = len(arr)
        nums = sorted(set(arr))
        ranks = {v:i+1 for i, v in enumerate(nums)}
        for i in range(n):
            arr[i] = ranks[arr[i]]
        return arr 

class SolutionV1:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n = len(arr)
        nums = list(set(arr))
        heapify(nums)
        ranks = {}
        rank = 1
        while nums:
            num = heappop(nums)
            ranks[num] = rank
            rank += 1
        
        for i in range(n):
            arr[i] = ranks[arr[i]]
        return arr
            

            


        
# @lc code=end

