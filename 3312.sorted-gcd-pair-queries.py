#
# @lc app=leetcode id=3312 lang=python3
#
# [3312] Sorted GCD Pair Queries
#

# @lc code=start
class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        freq = [0] * (mx + 1)
        for num in nums:
            freq[num] += 1 
        
        GCD = [0] * (mx + 1)

        for i in range(mx, 0, -1):
            # Count elements in nums that are multiples of i
            s = sum(freq[i::i])#sum all i and multiples of i

            total_pairs_with_divisor_i = s* (s-1)//2

            GCD[i] = total_pairs_with_divisor_i - sum(GCD[2*i::i])
        
        prefix_sum = list(accumulate(GCD))

        return [bisect.bisect_right(prefix_sum, q) for q in queries]
        
# @lc code=end

