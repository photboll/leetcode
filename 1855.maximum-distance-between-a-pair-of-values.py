#
# @lc app=leetcode id=1855 lang=python3
#
# [1855] Maximum Distance Between a Pair of Values
#

# @lc code=start
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        result = 0
        def bisect_right_desc(arr, target):
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = (lo + hi) // 2
                if arr[mid] >= target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        for i in range(n):  

            k = bisect_right_desc(nums2, nums1[i])
            print(f"{i, k-1}, {nums1[i], nums2[k-1]}")

            result = max(result, 
                        k - i -1
                         )
        return result
            


        
        


        
# @lc code=end

