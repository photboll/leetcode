#
# @lc app=leetcode id=2121 lang=python3
#
# [2121] Intervals Between Identical Elements
#

# @lc code=start
from collections import defaultdict
class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        intervals = [0] * len(arr)
        groups = defaultdict(list)

        for i, num in enumerate(arr):
            groups[num].append(i)

        for num, group in groups.items():
            total = sum(group)
            count = len(group)
            prefix = 0

            for i, idx in enumerate(group):
                #Number of elements to the left is i
                #number of element to the right is count -1 -i
                
                # som of idx - j for all indiced to the left of idx
                left_val = i * idx - prefix

                #find the proper suffix sum 
                right_sum = total - prefix - idx
                #sum of j - idx for all indices to the right of idx
                right_val = right_sum - (count -1 - i)*idx
                intervals[idx] = left_val + right_val

                prefix += idx


        return intervals
            



        
# @lc code=end

