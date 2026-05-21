#
# @lc app=leetcode id=2540 lang=python3
#
# [2540] Minimum Common Value
#

# @lc code=start
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        ptr1 = 0
        ptr2 = 0
        while ptr1 < len(nums1) or ptr2 < len(nums2):
            if nums1[ptr1] < nums2[ptr2]:
                if ptr1 < len(nums1) -1:
                    ptr1 += 1
                else:
                    return -1
            elif nums1[ptr1] > nums2[ptr2]:
                if ptr2 < len(nums2) -1:
                    ptr2 += 1
                else:
                    return -1
            else:
                return nums1[ptr1]
        return -1
        
# @lc code=end

