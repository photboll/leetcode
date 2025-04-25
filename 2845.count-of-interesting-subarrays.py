#
# @lc app=leetcode id=2845 lang=python3
#
# [2845] Count of Interesting Subarrays
#

# @lc code=start
from collections import Counter
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        prefix_counts = [0] * (n + 1)
        for i in range(n):
            prefix_counts[i+1]= prefix_counts[i] + (nums[i] % modulo == k)
        
        answer = 0

        #((prefix_counts[end] - prefix_counts[start]) % modulo == k)
        #prefic_counts[start] = (prefix_counts[end] + modulo - k) % modulo
        occurences = Counter()
        for i in range(n+1):
            paired_count = (prefix_counts[i] + modulo - k) % modulo
            answer += occurences[paired_count]
            occurences[prefix_counts[i] % modulo] += 1
        
                
        return answer 
    
        

        
# @lc code=end

