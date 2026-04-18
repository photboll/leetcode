#
# @lc app=leetcode id=3488 lang=python3
#
# [3488] Closest Equal Element Queries
#

# @lc code=start
from collections import defaultdict
from bisect import bisect_left

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        """
        we only actually need to now the position of the previous index and the first one(in the case we wrap around). we do not need to remember all of them
        for each new number we consider 
        fuck, 
        i misunderstood the question. one of the indices is fixed 
        """
        n = len(nums)
        num2is = defaultdict(list)

        for i, num in enumerate(nums):
            num2is[num].append(i)

        def get_circular_dist(i, j):
            d = abs(i -j)
            return min(d, n-d)
        
        result = []
        for q in queries:
            indices= num2is[nums[q]]
            if len(indices) <= 1:
                result.append(-1)
                continue

            k = bisect_left(indices, q) 
            left_neighbor = indices[k-1]
            right_neighbor = indices[(k+1) % len(indices)]
            result.append(min(
                get_circular_dist(q, left_neighbor),
                get_circular_dist(q, right_neighbor)
            ))

        return result
                
            



class SolutionWrong:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        """
        we only actually need to now the position of the previous index and the first one(in the case we wrap around). we do not need to remember all of them
        for each new number we consider 
        fuck, 
        i misunderstood the question. one of the indices is fixed 
        """
        
        n = len(nums)
        num2is = defaultdict(list)

        for i, num in enumerate(nums):
            li = num2is[num]
            if len(li) < 3:
                #[first_i, prev_i, cur_min]
                li.extend([i, i, float("inf")])
            else:
                first_i = li[0]
                prev_i = li[1]
                cur_min = li[2]

                cur_min = min(cur_min, 
                              abs(i-prev_i), #map to to previous
                              n - abs(i -first_i) # Wrap around
                              )
                li[1] = i
                li[2] = cur_min
        
        result = []
        for q in queries:
            res = num2is[nums[q]][2]
            result.append(-1 if res == float("inf") else res)
        return result
                
            



            


        
# @lc code=end

