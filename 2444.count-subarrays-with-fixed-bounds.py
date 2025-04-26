#
# @lc app=leetcode id=2444 lang=python3
#
# [2444] Count Subarrays With Fixed Bounds
#

# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        """
        Sliding window approach
        we keep expanding the window until we come across a number that is outside of [mink, maxk]
        so we never let any number that is outside the bounds ever enter the window at all
        all subarrays between left and right should then fixed bounds
        no wait, It is required that the min is equal to minK and the max == maxK
        so we need to keep track of the indices of the last seen minK and maxK
        or do we need to keep track of all previously seen minK and maxK? tha is within the window?
        It should be sufficient to only now the last seen 
        If a number is outside of the bounds then we should advance both left and right pointers regardless
         
        """
        n = len(nums)
        prev_maxK = -1
        prev_minK = -1
        l = 0
        count  = 0
        for r in range(n):
            num = nums[r]
            #if num is outside of [mink, maxK], then no array containing num can be fixed bounds
            if num < minK or num > maxK:
                l = r+1#Movve the begining of the window to after r
                continue

            #Add the current number to the window
            if num == minK:
                prev_minK = r
            if num == maxK:
                prev_maxK = r

            #Both minK and maxK have to be within the window for it to be a fixed bounds array 
            if prev_maxK < l or prev_minK < l:
                continue
                
            #The munber of subarrays ending at r that are fixd bounds, depends on min(last_minK_in_window, last_maxK_in_window)
            last_index = min(prev_maxK, prev_minK)
            #print(f"{l=} {last_index=} {r=} {count=} + {last_index-l+1}")
            #print([nums[s:r+1] for s in range(l, last_index+1)])
            count += last_index - l + 1

        return count 
                
        
# @lc code=end

