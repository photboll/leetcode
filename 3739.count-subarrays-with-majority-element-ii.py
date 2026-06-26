#
# @lc app=leetcode id=3739 lang=python3
#
# [3739] Count Subarrays With Majority Element II
#

# @lc code=start
class SolutionV2:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        pre = [0] * (n * 2 + 1)
        pre[n] = 1
        cnt = n 
        result = presum = 0

        for i in range(n):
            if nums[i] == target:
                presum += pre[cnt]
                cnt += 1
                pre[cnt] += 1
            else:
                cnt -= 1
                presum -= pre[cnt]
                pre[cnt] += 1
            result += presum
        return result 

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:

        n = len(nums)

        prefix = [0] * (n+1)

        for i, num in enumerate(nums):
            prefix[i+1] = prefix[i] + (1 if num == target else -1)

        
        size = 2 * n + 2
        bit = [0] * (size+1)

        def update(i):
            i += 1#1 indexed to get inclusive
            while i <= size:
                bit[i] += 1
                i += (i & -i)
        
        def query(i):
            i += 1
            s = 0

            while i > 0:
                s += bit[i]
                i -= i & -i
            return s
        
        result = 0

        for r in range(n + 1):
            v = prefix[r] + n

            if v > 0:
                result += query(v-1)
            update(v)

        return result 

    
        
# @lc code=end

