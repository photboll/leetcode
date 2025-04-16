#
# @lc app=leetcode id=2537 lang=python3
#
# [2537] Count the Number of Good Subarrays
#

# @lc code=start
from collections import Counter
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        """
        The equality makes it easier too count the number of pairs that get build for each number that we add to the window
        there ar etwo parts of this question.
        1. we need to know if a particualar subarray is good, i.e. how many pairs fullfill the criteria
        2. We need to count them all 
        so at each step we need to keep track how how many pairs of indices in the window fullfills the probelm
        the exact count of pairs is not important only the fact if its is more or less than k
        we know that any superarray of a good subarray must also be good. Since adding more numbers will never decrease the pair of counts 
        Can we use this to skip actually checkiing some of the posssible subarrays?
        as soon as our window contains at least k pairs, we can simply calculate the number of possible superarrays.
        And then decrease the window size by moving the left pointer forward.
        
        """
        count_good_subarrays = 0
        window_counts = Counter()
        pair_count = 0
        l = 0
        n = len(nums)
        for r in range(n):
            #we add nums[r] to the current window 
            window_counts[nums[r]] += 1
            #This may increase the number of pairs in the window
            #[1, 1, 1] add [1] would increase the number of pairs by the current count of 1
            pair_count += window_counts[nums[r]] -1
            
            #Does this make the window a good subarray?
            while pair_count >= k:
                #We need to calculate how many superarrays of the window exists 
                #Careful not to double count 
                #add every superarry that begins at the current starting point, l
                #We have another n - r possible elements to append to the current subarray
                #Which can only increase the pair_count 
                count_good_subarrays += n - r
                #print(l, r, count_good_subarrays, nums[l:r+1])
                
                #Now we should try to make the window smaller by moving the start point 
                #This will decrease the number of pairs in the window 
                window_counts[nums[l]] -= 1
                #But how many pairs will be removed when removing a sinlge number in the beginning?
                #is it 1 + ... + window_counts[nums[l]] ?
                pair_count -= window_counts[nums[l]]
                l += 1
            
            
        return count_good_subarrays

        
# @lc code=end

