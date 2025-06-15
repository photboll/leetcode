#
# @lc app=leetcode id=3357 lang=python3
#
# [3357] Minimize the Maximum Adjacent Element Difference
#

# @lc code=start
import itertools
import bisect
class Solution:
    def minDifference(self, nums: list[int]) -> int:
        maxPositiveGap = 0
        mn = 1_000_000_000
        mx = 0

        for a, b in itertools.pairwise(nums):
            if (a == -1) != (b == -1):
                positive = max(a, b)
                mn = min(mn, positive)
                mx = max(mx, positive)
            else:
                maxPositiveGap = max(maxPositiveGap, abs(a - b))

        #Perform binary search on the solution space
        low = maxPositiveGap# The largest abs diff of two adjacent positive integers in nums
        high = low + (mx - mn + 1) // 2
        #print(low, high)
        while low < high:
            mid = (low + high) //2
            if self._check(nums, mid, mn + mid, mx - mid):
                high = mid
            else:
                low = mid+1
        return low

    def _check(self, nums: list[int], m: int, x: int, y: int) -> bool:
        #given x and y will the maximum adjacent absolute difference be less than m?
        #We check each positive num in nums, 
        # Three main cases to check
        #1. a -1 is surounded by positive integers: single gap
        #2. there are multiple -1 in a row 
        #3. a -1 at the edge of nums, either at the start or the ending 
        gapLength = 0
        prev = 0

        for num in nums:
            if num == -1:
                gapLength += 1
                continue
            if prev > 0 and gapLength > 0:
                if gapLength == 1 and not self._checkSingleGap(prev, num, m, x, y):
                    return False
                if gapLength > 1 and not self._checkMultipleGaps(prev, num, m, x, y):
                    return False
            prev = num
            gapLength = 0

        
        #3. check the ends of the nums
        if nums[0] == -1:
            num = next((num for num in nums if num != -1), -1)#Find the first non -1 number
            if num != -1 and not self._checkBoundaryGaps(num, m, x, y):
                return False

        if nums[-1] == -1:
            num = next((num for num in reversed(nums) if num != -1), -1)# Find the last non-1 number
            if num != -1 and not self._checkBoundaryGaps(num, m, x, y):
                return False

        return True

    def _checkSingleGap(self, a: int, b: int, m: int, x: int, y: int) -> bool:
        #Determine which of x and y will minimize the difference
        gapWithX = max(abs(a - x), abs(b - x))
        gapWithY = max(abs(a - y), abs(b - y))
        #check if the minimum is good enough 
        return min(gapWithX, gapWithY) <= m

    def _checkMultipleGaps(self, a: int, b: int, m: int, x: int, y: int) -> bool:
        ax = abs(a - x)
        ay = abs(a - y)
        bx = abs(b - x)
        by = abs(b - y)
        xy = abs(x - y)
        gapAllX = max(ax, bx)
        gapAllY = max(ay, by)
        gapXToY = max(ax, xy, by)
        gapYToX = max(ay, xy, bx)
        return min(gapAllX, gapAllY, gapXToY, gapYToX) <= m

    def _checkBoundaryGaps(self, a: int, m: int, x: int, y: int) -> bool:
        gapAllX = abs(a - x)
        gapAllY = abs(a - y)
        return min(gapAllX, gapAllY) <= m

class SolutionV2WRong:
    def minDifference(self, nums):
        neighbors = set()
        has_missing_vals = False
        has_adjacent_missing = False
        max_abs_adj_diff = float("-inf")
        for i in range(len(nums)):
            if nums[i] == -1:
                has_missing_vals = True
                if i > 0 and nums[i-1] == -1:
                    has_adjacent_missing = True
            for neighbor in [i-1, i+1]:
                if 0 <= neighbor < len(nums) and nums[neighbor] != -1:
                    neighbors.add(neighbor)
                    max_abs_adj_diff = max(max_abs_adj_diff, abs(nums[i] - neighbor))
                    
        if not has_missing_vals:
            return max_abs_adj_diff
        
        
        neighbors = sorted(list(neighbors))

        def is_possible(d: int) -> bool:
            if d < max_abs_adj_diff:
                return False
            
            # [l, u] is the valid range for the first replacement number 'x'
            l, u = 1, float('inf')
            
            for i in range(len(neighbors)):
                v = neighbors[i]
                v_range_l, v_range_u = v - d, v + d
                
                # If current range [l, u] has no overlap with v's required range
                if u < v_range_l or l > v_range_u:
                    # Break point. 'x' covers neighbors[0...i-1].
                    # 'y' must cover neighbors[i...n-1].
                    
                    # Range for 'x' is [l, u] which we already have.
                    lx, ux = l, u
                    
                    # Range for 'y' is the intersection of requirements for the rest.
                    ly = neighbors[-1] - d
                    uy = neighbors[i] + d
                    
                    if max(1, ly) > uy: # 'y' range is invalid
                        return False
                    
                    # THE CRUCIAL CHECK: can we pick x and y to be close enough?
                    # This check is only necessary if there's a possibility of
                    # x and y being adjacent (i.e., a block of two or more -1's).
                    if has_adjacent_missing:
                        # Check if ranges [lx, ux] and [ly, uy] are at most d apart.
                        if max(lx, ly) - min(ux, uy) > d:
                             return False
                    
                    return True # Found a valid partition
                
                # No break, so 'x' must also cover v. Shrink the range for 'x'.
                l = max(l, v_range_l)
                u = min(u, v_range_u)

            # If we never broke, one number 'x' can cover all neighbors.
            return max(1, l) <= u
                    
            
            
        low = max_abs_adj_diff
        high = max(nums)
        while low < high:
            mid = (high + low) // 2
            
            if is_possible(mid):
                high = mid
            else:
                low = mid+1

        return low
            
class SolutionWRONG:
    def minDifference(self, nums: List[int]) -> int:
        """
        We can only affect the absolute difference of numbers that are directly adjacent to a -1
        we want to minimize a maximum value which hints at using a binary search approch on the solution space.
        What range is our solution space? the absolute minimal possible absolute difference
        is the min difference of any two neighbors. in ex 1 the 10 and 8 gives a absolute difference of 2
        so any solution needs to be larger than or equal to two
        The interior of any substring of -1 should be filled uniformly. no it is not always possible to do this,
        we can only select two postiive integers x and y
        
        Maybe it helps to solve a similar alternative problem.
        What happens if we are allowed to choose as many digits as we want?
        What happens if we consider it for a fixed pair of digits?
        """
        
        #How do we check if there exist a pair (x,y) that gives maximum absolute difference of mid?
        def is_possible(val):
            #For a given value checks if it is possible to find x and y such that the max abs diff < value
            lower_bound, upper_bound= get_feasible_range(nums, val)
            #print(lower_bound, upper_bound, lower_bound<= upper_bound)
            return lower_bound <= upper_bound
        
        def get_feasible_range(nums, val):
            upper_bound, lower_bound = float("inf"), float("-inf")
            for i in range(len(nums)):
                if nums[i] != -1:
                    continue
                
                for neighbor in [i-1, i+1]:
                    #is the neighbor within bounds and not -1
                    if 0 <= neighbor < len(nums) and nums[neighbor] != -1:
                        upper_bound = min(upper_bound, nums[neighbor] + val)
                        lower_bound = max(lower_bound, nums[neighbor] - val)
                
            return lower_bound, upper_bound

        contains_neg = nums[0] == -1
        max_abs_adj_diff = float("-inf")
        for i in range(1, len(nums)):
            if nums[i] == -1:
                contains_neg = True
            elif nums[i-1] != -1:
                max_abs_adj_diff = max(max_abs_adj_diff, abs(nums[i] - nums[i-1]))

            
        low = 0
        high = max(nums)
        #if the ceiling is negative then all entries of nums must be negative, so we can choose everyon to be equal eachother
        if all(num == -1 for num in nums):
            return 0
        elif not contains_neg:
            return max_abs_adj_diff
                    
        
        while low < high:
            mid = (low+high) // 2
            #print(low, mid, high)
            if is_possible(mid):
                high = mid
            else:
                low = mid + 1
        
        return max(low, max_abs_adj_diff)
        
        
        
        
        
# @lc code=end


