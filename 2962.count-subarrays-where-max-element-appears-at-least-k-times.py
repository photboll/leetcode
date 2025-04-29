#
# @lc app=leetcode id=2962 lang=python3
#
# [2962] Count Subarrays Where Max Element Appears at Least K Times
#

# @lc code=start
from collections import deque
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """
        Sliding window:
        any superarray of a subarray which have at least K target will also be avalid array 
        it might be easier to just go through the subarrays in order and add +1 as long 
        as we have atleasst k elements in the window. no wait, 
        the problem is where is the beginning of each such subarray.
        
        we will keep track of each target seen in a buffer of k elemnts 
        for each possible end point of an aubarray we can then quickly lookup,
        which start point is the last possible one,
        """
        target = max(nums)
        target_idxs = deque()
        count = 0
        n = len(nums)
        for right in range(n):
            if nums[right] == target:
                target_idxs.append(right)
            
            if len(target_idxs) > k:
                #cap the size of the buffer at k
                target_idxs.popleft() 
            if len(target_idxs) == k:
                #Every array that ends at right and begins
                #before the first element in the buffer will have atleast k target
                #+1 since the both the start and end is inclusive
                #print(nums[:right+1], target_idxs[0] ,count, target_idxs)
                count += target_idxs[0]+1
        return count
            

        
        
# @lc code=end

