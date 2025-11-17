#
# @lc app=leetcode id=1437 lang=python3
#
# [1437] Check If All 1's Are at Least Length K Places Away
#

# @lc code=start
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev_one = -1
        
        for i in range(len(nums)):
            #print(i, prev_one)
            if nums[i] == 1:
                if prev_one > -1 and i - prev_one -1 < k:
                    return False

                prev_one = i
                
        return True
        
# @lc code=end

