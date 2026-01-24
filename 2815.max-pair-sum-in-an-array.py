#
# @lc app=leetcode id=2815 lang=python3
#
# [2815] Max Pair Sum in an Array
#

# @lc code=start
from collections import defaultdict

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        result = -1

        def largest_digit(x: int) -> int:
            res = -1
            while x > 0:
                x, digit = divmod(x, 10)
                res = max(res, digit)
            return res
        
        digit2pair = defaultdict(list)

        for x in nums:
            dig = largest_digit(x)
            l = digit2pair[dig]
            l.append(x)
            if len(l) > 2:
                l.sort()
                l = l[-2:]
            if len(l) == 2:
                result = max(result, sum(l))
            digit2pair[dig] = l
        #print(digit2pair)
        return result


        
# @lc code=end

