#
# @lc app=leetcode id=1792 lang=python3
#
# [1792] Maximum Average Pass Ratio
#

# @lc code=start
from heapq import heappop, heappush, heapify

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        """
        We want to add the extra stduents were they will increase the pass ratio the most 
        they will increase the pass ratio the most if we always add them to the class total student,
        or is it the fewest passing students. NO the contribution to the total average pass ratio is proportional to the number of 
        total students in the calss
        """

        def calc_gain(passing, total):
            return (passing + 1) / (total + 1) - passing / total

        heap = []

        for passing, total in classes:
            heap.append((-calc_gain(passing, total), passing, total ))

        heapify(heap)
        
        for _ in range(extraStudents):
            _, cur_pass, cur_tot = heappop(heap)
            heappush(heap, (
                -calc_gain(cur_pass+1, cur_tot+1),
                cur_pass + 1,
                cur_tot + 1)
                     )
        
        
        res = 0
        for _, passing, tot in heap:
            res += passing / tot
        
        return res / len(classes)

            


        
# @lc code=end

