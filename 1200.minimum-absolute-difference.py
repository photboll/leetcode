#
# @lc app=leetcode id=1200 lang=python3
#
# [1200] Minimum Absolute Difference
#

# @lc code=start
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        arr.sort()
        n = len(arr)
        result = []
        min_abs_diff =  float("inf")
        for i in range(1, len(arr)):
            min_abs_diff = min(min_abs_diff, arr[i] - arr[i-1])
        
        for i in range(1, n):
            if arr[i] - arr[i-1] == min_abs_diff:
                result.append([arr[i-1], arr[i]])
        return result
        
        
        
                
            

            

        
# @lc code=end

