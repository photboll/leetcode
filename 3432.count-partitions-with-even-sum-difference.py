#
# @lc app=leetcode id=3432 lang=python3
#
# [3432] Count Partitions with Even Sum Difference
#

# @lc code=start
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        s = sum(nums)

        res = 0
        tot = 0
        for num in nums[:-1]:
            tot += num
            s -= num
            if (s - tot) % 2 == 0:
                res += 1
        return res
        
# @lc code=end

