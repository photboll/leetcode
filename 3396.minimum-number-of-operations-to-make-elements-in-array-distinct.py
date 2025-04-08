#
# @lc app=leetcode id=3396 lang=python3
#
# [3396] Minimum Number of Operations to Make Elements in Array Distinct
#

# @lc code=start
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        latest_duplicate = -1
    
        for i in range(len(nums)-1, -1, -1):
            if nums[i] in seen:
                latest_duplicate = i
                break
            else:
                seen.add(nums[i])
        #print(latest_duplicate)
        #There was no duplicate
        if latest_duplicate == -1:
            return 0
            
        return latest_duplicate // 3 + 1
        
# @lc code=end

