#
# @lc app=leetcode id=918 lang=python3
#
# [918] Maximum Sum Circular Subarray
#

# @lc code=start
def maxSubarraySum(nums):
    max_sum = float("-inf")
    current_sum = 0
    for num in nums:
        #Either we start a new array at this location 
        #or we extend the previous array
        current_sum = max(current_sum + num, num)
        #Did starting a new array or extending it beat the best sum seen so far
        max_sum = max(max_sum, current_sum)
    
    return max_sum       

def minSubarraySum(nums):
    min_sum = float("inf")
    current_sum = 0
    for num in nums:
        current_sum = min(current_sum + num, num)
        min_sum = min(min_sum, current_sum)
    return min_sum

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        Either best subarray sum is contained in the middle of the array, in which case regular kadanes 
        will find it 
        [... {...MAX...}...]
        or the sum array consists of the concatenate of a subarrya begining at 0 and on ending at n-1
        [MAX...} ...  { ...MAX]
        Both cases are partitions of the original array into three parts,
        We alos know that the total sum of the entire array is the same in both cases 
        Total = part1 + part2 + part3
        in Case 1 the requested answer is the sum of part 2
        In case 2 we know that the  sum part1 + part3 is the requested answer.
        Can we modify kadane and reuse it in the second case to answer the question?
        Wait maybe it is easierr to interpret the two cases as partitioning the array into two parts instead.
        in case1: Kadane gives us part2 using the total equation we get part1 + part3 = Total - part2
        Lets regroup the total sum 
        Total = (part1 + part3) + part2
        
        We also know that the maxium subarray sum + the minimum subarray sum should always equal the total
        Is it so that in both cases the remaining unknwon part is simply the minimum subarray sub? 
        """
        total = sum(nums)
        max_subarray_sum = maxSubarraySum(nums)
        min_subarray_sum = minSubarraySum(nums)
        if max_subarray_sum < 0:
            #Then nums must only have negative numbers
            #Since we cant choose 0length subbarays
            #we have to choose case 1 
            #Since choosing case 2 implies that the max_subarray has zero length
            return max_subarray_sum
        return max(max_subarray_sum, total- min_subarray_sum)
# @lc code=end

