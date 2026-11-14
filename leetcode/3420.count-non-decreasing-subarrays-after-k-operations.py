# @lc app=leetcode id=3420 slug=count-non-decreasing-subarrays-after-k-operations lang=python3
#
# [3420] Count Non-Decreasing Subarrays After K Operations
# Difficulty: Hard
# Tags: Array, Stack, Segment Tree, Queue, Sliding Window, Monotonic Stack, Monotonic Queue
# URL: https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/
#
# @lc code=start
from heapq import heappush, heappop
class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        #
        n = len(nums)
        result = 0
        operations = 0
        #pq to maintain a windows max
        pq = []

        cnt = [[] for _ in range(n)]

        #index of the first >= to the right
        pos = [n] * n
        stack = [0]# decreasing monotonic

        l = 0
        for r in range(n):
            # maintain the monotonic stack
            while stack and nums[r] >= nums[stack[-1]]:
                pos[stack.pop()] = r
            
            #the stack top is the nearest greater element to the left of the current
            if stack:
                cnt[stack[-1]].append(r)

            stack.append(r)

            #pq fron is the window max
            heappush(pq, (-nums[r], r))
            # adding nums[r] incease the number of operations used
            operations += max(0, -pq[0][0] - nums[r])

            #if number of operations exceeds k: shrink the window
            while operations > k:
                for i in cnt[l]:
                    #subtract the contribution of the leftmost element
                    operations -= (
                        (nums[l] - nums[i] ) * (min(pos[i], r + 1) - i)
                    )
                l += 1
            
            # remove the removed  form the pq
            while pq and pq[0][1] < l:
                heappop(pq)
            
            #there are right - left + 1 valid subarrays ending at r
            result += r - l + 1

        return result


                

        

# @lc code=end
