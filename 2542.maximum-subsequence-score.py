#
# @lc app=leetcode id=2542 lang=python3
#
# [2542] Maximum Subsequence Score
#

# @lc code=start
from heapq import heappush, heappop 
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """
        is it best to select indics based on nums2[i] where we select the k largest from there.
        proabbly not, if there is only a small difference between nums2[i] and nums2[j] but a huge difference 
        nums1[i] and nums1[j] then it would be better to select the large value of i and j
        all numbers are positive as well and integers, we never want to select i where nums2[i]== 0 unless we are forced to

        we want to consider each tuple of (nums1[i], nums2[i], i) is it better to keep it in the selection or not?
        if nums2[i] is larger then the current minimum of nums2 then it
        lets assume we have  selection of indices k indices [2, 3]  and we want which index is best to consider for exclusion?
        and whcih index outside of our selection is best to consider for inclusion into the selection. 

        if k == 1: the problem reduces into simply finding the i for which nums1[i] * nums2[i] is the largest 
        ut shoul dbe possible to iterate using this, at each step we want to add the number tha maximizes
        this is not it, it ends up being wron 
        """
        n = len(nums1)
        tuples = [(i, nums1[i], nums2[i]) for i in range(n)]
        tuples.sort(key= lambda x: -x[2])
        print(tuples)
        curr_sum = 0
        max_score = 0
        heap = []
        for i, num1, num2 in tuples:
            #let num2 be the minimum value of our selection,
            #since we have sorted by num2
            #we are free too choose any selection previously seen num1 
            # actually we have to always choose the current num1, or else min2 would be larger than num2
            #but this scenario would have already been considered aleady
            curr_sum += num1
            heappush(heap, num1)
            if len(heap) > k:     
                prev_num = heappop(heap) 
                curr_sum -= prev_num

            if len(heap) == k:
                #print(num1, num2, max_score, curr_sum * num2, heap)
                max_score = max(max_score, curr_sum * num2)
            
             
        return max_score       


        
# @lc code=end

