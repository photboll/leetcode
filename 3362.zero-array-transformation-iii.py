#
# @lc app=leetcode id=3362 lang=python3
#
# [3362] Zero Array Transformation III
#

# @lc code=start
from heapq import heappop, heappush
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key= lambda x: x[0])

        pq = []
        diff = [0] * (len(nums) + 1)
        operations = 0
        j = 0
        
        for i, num in enumerate(nums):
            operations += diff[i]
            while j < len(queries) and queries[j][0] == i:
                heappush(pq, -queries[j][1])
                j += 1
            while operations < num and pq and -pq[0] >= i:
                operations += 1
                diff[-heappop(pq) + 1] -= 1
            
            if operations < num:

                return -1
        return len(pq)
        
# @lc code=end

