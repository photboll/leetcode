#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in range(len(nums1)):
            j = nums2.index(nums1[i])
            nxt = -1
            for k in range(j+1, len(nums2)):
                if nums2[k] > nums2[j]:
                    nxt = nums2[k]
                    break
            result.append(nxt)
        return result
        
# @lc code=end

