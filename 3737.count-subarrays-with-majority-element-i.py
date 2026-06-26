#
# @lc app=leetcode id=3737 lang=python3
#
# [3737] Count Subarrays With Majority Element I
#

# @lc code=start
class SolutionV1:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        
class SolutionV1:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        result = 0
        prefix = [0] * (n + 1)  # prefix[i] = count of target in nums[0..i-1]

        for r in range(n):
            prefix[r + 1] = prefix[r] + (1 if nums[r] == target else 0)
            for l in range(r + 1):
                count = prefix[r + 1] - prefix[l]
                length = r - l + 1
                if count * 2 > length:  # strictly more than half
                    result += 1
        return result
                    



        
# @lc code=end

