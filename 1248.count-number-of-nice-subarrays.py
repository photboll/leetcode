#
# @lc app=leetcode id=1248 lang=python3
#
# [1248] Count Number of Nice Subarrays
#

# @lc code=start
from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums, k):
        count = 0
        prefix_sum = 0
        freq = defaultdict(int)
        freq[0] = 1#the empty prefix sum occurs once
        
        for num in nums:
            prefix_sum += num %2
            count += freq[prefix_sum-k]
            freq[prefix_sum] += 1
        return count
class SolutionV1:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
        Sliding window approach, 
        what matters is the number of odd numbers in the window
        """
        n = len(nums)
        for i in range(n):
            nums[i] %= 2
        
        prefix = [0] * (n+1)
        prefix[0] = 0
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + nums[i-1]
        #print(prefix)
        count = 0
        left = 0
        for right in range(1, n+1):      
            for left in range(right):
                odd_nums_in_window = prefix[right] - prefix[left]
                if odd_nums_in_window== k:
                    count += 1
                elif odd_nums_in_window < k:
                    break
                
        return count
                
        
            
            
                
            
            
            
        
# @lc code=end

