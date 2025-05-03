#
# @lc app=leetcode id=2215 lang=python3
#
# [2215] Find the Difference of Two Arrays
#

# @lc code=start
def findDifference(nums1, nums2):
    return list(set(nums1).difference(set(nums2)))

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [findDifference(nums1, nums2), findDifference(nums2, nums1)]
        
# @lc code=end

