#
# @lc app=leetcode id=2163 lang=python3
#
# [2163] Minimum Difference in Sums After Removal of Elements
#

# @lc code=start
from heapq import heappush, heappushpop
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        """
        Bruteforce will be two slow, combination pick n from 3n number of need to be considered
        n can be at most 10_000 which is too large to brute force.
        
        the difference of sums will be minimal if we try to minimize sum_first and maximize sum_sec
        can we use this to rank each num?
        
        considering a single num at a time.
        if it is in the first third of nums: then it can belong to sum1 or be excluded
        if it is in the secon third of nums: then it can belong to sum1, sum2, or be excluded
        if it is in the third third of nums: then it can belong to sum2 or be excluded   
        
        Can we start with an initial assignment and then search for the best solution?
        This wont work, we cant freely re-assign integers between the groups. since their order is fixed. 
        
        What is the recursive property here?
        
        Hint1: was the above mention minimize/maximize
        Hint2:For every index i, think about how you can find the minimum possible sum of n elements with indices lesser or equal to i, if possible.
        if i < n then it is impossible
        we can use a max heap, fill it with numbers as soon as the size of the heap exceeds n
        we will push the cuurrent value and then pop the max. The total sum of the heap will then be minimized
        We keep track of the current sum of the heap as well, to efficiently know the sum for all indexes
        
        can we then do the opposite thing form the other end? and then compare the states?
        """
        n = len(nums) // 3
        heap = []
        heap_sum = 0
        min_sum_upto = [None] * len(nums)

        for i in range(len(nums)):
            #REMEMBER: heapq is a minheap, need to negate values to get max heap
            if len(heap) < n:
                heappush(heap, -nums[i])
                heap_sum += nums[i]
            else:
                popped_num = heappushpop(heap, -nums[i])
                heap_sum += nums[i] + popped_num

            if len(heap) == n:
                min_sum_upto[i] = heap_sum

                
                
        heap = []
        heap_sum = 0
        max_sum_starting = [None] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            if len(heap) < n:
                heappush(heap, nums[i])
                heap_sum += nums[i]
            else:
                popped_num = heappushpop(heap, nums[i])
                heap_sum += nums[i] - popped_num

            if len(heap) == n:
                max_sum_starting[i] = heap_sum
                
        #print(min_sum_upto)
        #print(max_sum_starting)
        
        
        res = float("inf")
        for i in range(n - 1, 2 * n):
            sum1 = min_sum_upto[i]
            sum2 = max_sum_starting[i + 1]
            res = min(res, sum1 - sum2)
        return res
        
        
        


        
        
# @lc code=end

