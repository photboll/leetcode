from typing import List
#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsetsV3(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        def backtrack(start):
            result.append(subset[:])
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()
        backtrack(0)
        return result
                
    def subsetsV2(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        return [[nums[j] for j in range(n) if (i >> j) & 1] for i in range(1 << n)]
    
    def subsetsV1(self, nums: List[int]) -> List[List[int]]:
        results = []
        n = len(nums)
        for i in range((1 << n), (1 << (n+1))):
            res = []
            mask = bin(i)[3:]
            for j, char in enumerate(mask):
                if char == "1":
                    res.append(nums[j])
            results.append(res)
        return results

# @lc code=end
import timeit
def benchmark(size, number):
    sol = Solution()
    test_nums = list(range(size))  # Adjust this size based on performance needs
    
    time_v1 = timeit.timeit(lambda: sol.subsetsV1(test_nums), number=number)
    time_v2 = timeit.timeit(lambda: sol.subsetsV2(test_nums), number=number)
    time_v3 = timeit.timeit(lambda: sol.subsetsV3(test_nums), number=number)
    
    print(f"subsetsV1 (original bit manipulation): {time_v1:.6f} seconds")
    print(f"subsetsV2 (optimized bit manipulation): {time_v2:.6f} seconds")
    print(f"subsetsV3 (backtracking): {time_v3:.6f} seconds")


if __name__ == "__main__":
    benchmark(20, 20)

