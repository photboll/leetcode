#
# @lc app=leetcode id=3430 lang=python3
#
# [3430] Maximum and Minimum Sums of at Most Size K Subarrays
#

# @lc code=start
from collections import deque

def get_min_sum(nums, k):
    min_sum = curr_sum = 0
    q = deque()
    for i, num in enumerate(nums):
        if i>= k:
            q[0][1] -= 1
            curr_sum -= q[0][0]
            if q[0][1] == 0:
                q.popleft()
        curr_len = 1
        curr_sum += num
        while q and q[-1][0] > num:
            prev_num, prev_len = q.pop()
            curr_sum += num * prev_len - prev_num * prev_len
            curr_len += prev_len
        
        q.append([num, curr_len])
        min_sum += curr_sum
    return min_sum
                
class Solution:
    def minMaxSubarraySum(self, nums: List[int], k: int) -> int:
        min_sum = get_min_sum(nums, k)
        max_sum = -get_min_sum([-x for x in nums], k)
        return min_sum + max_sum

class SolutionV1:
    def minMaxSubarraySum(self, nums: List[int], k: int) -> int:
        """  
        keep tra k of the 
        """
        #nums[0:1] have min+max 
        n = len(nums)
        #the queue should hold max values in the order the appear 
        #we will prune it so all indexes is ge r - k
        dec_q = deque()
        max_sum = 0

        print(nums)
        for r in range(n):
            #r is the endpoint 
            # consider subarrays from max(0, r - k):r
            
            #remove dominated nums, any subarray ending at r can at worst have nums[r] as its maximum 
            while dec_q and dec_q[-1][0] <= nums[r]:
                dec_q.pop()
            
            #add current element to window
            dec_q.append((nums[r], r))
            
            #remove out of scope elements
            if dec_q[0][1] < r- k+1:
                dec_q.popleft()

            
            l = max(0, r-k+1)

            cur_max = dec_q[0][0]
            #how many subarrays ends at r? that are smaller than k
            count = r - l + 1
            max_sum += count * cur_max
            print(l, r,nums[l:r+1], dec_q, cur_max, count, max_sum)

        
        #Flip it and do the corresponding for minimum
        inc_q = deque()
        min_sum = 0 
        for l in range(n-1, -1, -1):
            while inc_q and inc_q[-1][0] >= nums[l]:
                inc_q.pop()

            inc_q.append((nums[l], l))

            r = min(n-1, l + k-1)
            if inc_q[0][1] > r:
                inc_q.popleft()

            cur_min = inc_q[0][0]
            count = r - l + 1
            min_sum += count * cur_min
            print(l, r,nums[l:r+1], inc_q, cur_min, count, min_sum)
        return min_sum + max_sum
            
            

            
# @lc code=end

