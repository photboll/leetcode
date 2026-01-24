#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
from collections import deque
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1]* n
        q = deque()

        for j in range(2*n-1, -1, -1):
            i = (j % n)
            x = nums[i]

            while q and nums[q[-1]] <= x:
                q.pop()
            
            if q:
                result[i] = nums[q[-1]]
            else:
                result[i] = -1

            q.append(i)

        return result


        
# @lc code=end

