#
# @lc app=leetcode id=3495 lang=python3
#
# [3495] Minimum Operations to Make Array Elements Zero
#

# @lc code=start
from math import log, floor
class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:

        def ops_to_reduce_query(l, r):
            num_divs = 0
            prev_s = 1
            curr_s = 4
            k = 1
            
            while prev_s <= r:
                a = max(l, prev_s)
                b = min(r, curr_s -1)

                ##print(prev_s, curr_s, k, (a, b))
                #if [prev_s, curr_s] overlaps with [l, r]
                if b >= a:
                    overlapping_count = b - a + 1 # + 1 including endpoints 
                    #each number in the current overlap needs the same amount of divisions
                    #to reach zero. Which is k 
                    num_divs += overlapping_count * k

                prev_s = curr_s
                curr_s *= 4
                k += 1
            
            return (num_divs+ 1) // 2
        
        result = 0
        for query in queries:
            result += ops_to_reduce_query(*query)
        
        return result

        
# @lc code=end

