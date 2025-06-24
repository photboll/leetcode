#
# @lc app=leetcode id=2200 lang=python3
#
# [2200] Find All K-Distant Indices in an Array
#

# @lc code=start
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n  = len(nums)
        close_to_key = [False] * n

        
        for i, num in enumerate(nums):
            if num == key:
                for j in range(max(i-k, 0), min(i+k+1, n)):
                    close_to_key[j] = True
        
        result = []
        for i in range(n):
            if close_to_key[i]:
                result.append(i)
        return result
        
        
# @lc code=end

