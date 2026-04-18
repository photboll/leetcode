#
# @lc app=leetcode id=3761 lang=python3
#
# [3761] Minimum Absolute Distance Between Mirror Pairs
#

# @lc code=start
class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:

        def reverse(num: int) -> int:
            res = 0
            while num > 0:
                res *= 10
                num, rem = divmod(num, 10)
                res += rem
            return res

        #print(reverse(120), reverse(543123), reverse(4500000))

        prev_i = {}
        res = float("inf")
        
        for i, num in enumerate(nums):
            try:
                res = min(res, 
                          abs(prev_i[num] - i))
            except KeyError:
                pass

            reverse_num = reverse(num)
            prev_i[reverse_num] = i
        return res if res < float("inf") else -1
                
        
# @lc code=end

