#
# @lc app=leetcode id=611 lang=python3
#
# [611] Valid Triangle Number
#

# @lc code=start
from itertools import combinations
class Solution:
    def triangleNumber(self, nums):
        nums.sort()
        n = len(nums)
        total = 0
        
        for k in range(n-1, 1, -1):
            #nums[k] = c
            #nums[r] = b
            #nums[l] = a
            # since nums is sorted a <= b <= c
            l, r = 0, k-1
            while l < r:
                if nums[l] + nums[r
                                  ] > nums[k]:
                    #then all pairs in (i,..., j) are valid
                    total += r -l 
                    r -= 1
                else:
                    #We need to make a + b larger
                    # b already at max, can only increase a
                    l += 1 
        return total 
class SolutionBS:
    def triangleNumber(self, nums):
        def bs(a, b, start_i):
            lb = start_i
            ub = n
            while lb < ub:
                mid = (lb + ub )// 2 
                #print(lb, mid, ub)
                if a + b > nums[mid]:
                    lb = mid + 1
                else:
                    ub = mid
            
            return lb 
                    
            
        nums.sort()

        n = len(nums)
        total = 0
        for i in range(n):
            a = nums[i]
            for j in range(i+1, n-1):
                b = nums[j]
                # a + b > c must be true for all triangles
                # a + c > b and b + c > a will be always be true since c is always the longest side
                #Since we have sorted the nums
                #Which is the smallest c that makes the condition true
                #binary search
                idx = bs(a, b, j+1)
                count = idx - (j+1)
                total += count
                
        return total 
                
                
class SolutionBF:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        What is a valid triangle number?
        the sum of two sides have to be greater than the third side.
        
        should I check all combinations if they are valid triangle nubmers
        or is their a smarter approach.
        maybe sorting them and check them in a certain order, as soon as one side gets out of bounds, we can prine a large part of the search space
        """

        def is_triangle(a, b, c):
            return a + b > c and b + c > a and a + c > b
        
        total = 0
        for comb in combinations(nums, 3):
            total += is_triangle(*comb)
                
        return total 
            


        
# @lc code=end

