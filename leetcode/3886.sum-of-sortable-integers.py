# @lc app=leetcode id=3886 slug=sum-of-sortable-integers lang=python3
#
# [3886] Sum of Sortable Integers
# Difficulty: Hard
# Tags: Array, Math, Sorting, Enumeration
# URL: https://leetcode.com/problems/sum-of-sortable-integers/
#
# @lc code=start
class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)

        total = 0

        for k in range(1, n+1):
            if n% k:
                continue

            ok = True

            prev_max = 0

            for s in range(0, n, k):
                # count cyclic descents within the block

                desc = 0

                for i in range(k):
                    if nums[s+i]  > nums[s+(i+1) % k]:
                        desc += 1
                        if desc > 1:
                            break
                    
                if desc > 1:# no descending steps are allowed
                    ok = False
                    break
            
                block = nums[s:s+k]
                lo, hi = min(block), max(block)

                if lo < prev_max:
                    ok = False
                    break
                prev_max = hi
        
            if ok:
                total += k
        return total 
                
                
        

# @lc code=end
