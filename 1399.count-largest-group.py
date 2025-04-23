#
# @lc app=leetcode id=1399 lang=python3
#
# [1399] Count Largest Group

# @lc code=start
from collections import defaultdict
class Solution:
    def countLargestGroup(self, n: int) -> int:
        #n is constrained to amximum of 10000 so a brute force solution should work 
        groups =  defaultdict(list)
        largest_group_size = 0
        count_largest_size = 0
        def digitSum(num):
            tot = 0
            while num > 0:
                num, rem = divmod(num, 10)
                tot += rem
            return tot
        for i in range(1, n+1):
            cur_sum = digitSum(i)
            cur_group = groups[cur_sum]
            #add tje current digit sum to its group
            cur_group.append(i)
            #Did it equal tge largest group?
            if len(cur_group) == largest_group_size:
                count_largest_size += 1
            #Did that make the current group larger
            elif len(cur_group) > largest_group_size:
                #Then we currently only have single group of this size 
                count_largest_size = 1
                largest_group_size = len(cur_group)

        return count_largest_size 
            
        
# @lc code=end

