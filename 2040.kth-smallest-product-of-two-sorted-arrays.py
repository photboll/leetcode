#
# @lc app=leetcode id=2040 lang=python3
#
# [2040] Kth Smallest Product of Two Sorted Arrays
#

# @lc code=start
import math, bisect
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """
        Four cases, every combination of signs possible when taking num from nums1 and nums2
        - + and + - will give the smallest possible values 
        - - and + + will give larger values
        Is it binary search on the solution space?
        do we actually need to find the values that makes the product or can we find the kth product without knowing the factors themselves? 
        can we quickly determine in what range the products must be in?
        nums1[0] * nums2[0] can give the min if they have different signs, if both are negative then it can give the max
        nums1[0] * nums2[-1] Same thing 
        nums1[-1]* nums2[0] same as above
        nums1[-1]* nums[-1] same as above.
        So the max of these four values is the upper bound and the min is the lower bound.
        Can we use this fact to iteratively chop the ends of the nums arrays? until the upper and lower bound converges on a single number?
        
        """


        def prod_count_le(x: int) -> int:
            count = 0
            for a in nums1:
                if a == 0:
                    if mid >= 0:
                        count += len(nums2)
                elif a > 0:
                    # b <= mid / a
                    t = mid / a
                    idx = bisect.bisect_right(nums2, math.floor(t))
                    count += idx
                else:  # a < 0
                    # b >= ceil(mid / a)
                    t = mid / a
                    thr = math.ceil(t)
                    idx = bisect.bisect_left(nums2, thr)
                    count += len(nums2) - idx
            return count
            
        
        
        #Let nums1 be the shorter of the two lists 
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
            
        
        a = nums1[0] * nums2[0]
        b = nums1[0] * nums2[-1]
        c = nums1[-1] * nums2[0]
        d = nums1[-1] * nums2[-1]
        low = min(a,b,c,d)
        high = max(a,b,c,d)

        while low < high:
            mid = low + (high - low) // 2
            
            if prod_count_le(mid) >= k:
                high = mid
            else:
                low = mid+1
                
        
        return low
        
# @lc code=end

