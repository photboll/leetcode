#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        #q should remain monotonic decreasing 
        q = deque()

        result = []
        for r in range(n):
            #remove indices which are outside of the current window
            if q and q[0] <= r - k:
                q.popleft()
            
            #remove all indices which have a value less than current
            #as they will never become the maximum again 
            while q and nums[q[-1]] <= nums[r]:
                q.pop()
            
            q.append(r)

            if r >= k -1:
                #the front of the queue will always have the maximum value
                result.append(nums[q[0]])
        
        return result 


        
# @lc code=end

