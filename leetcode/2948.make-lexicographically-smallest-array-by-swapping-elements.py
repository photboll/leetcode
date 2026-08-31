# @lc app=leetcode id=2948 slug=make-lexicographically-smallest-array-by-swapping-elements lang=python3
#
# [2948] Make Lexicographically Smallest Array by Swapping Elements
# Difficulty: Medium
# Tags: Array, Union-Find, Sorting
# URL: https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/
#
# @lc code=start
from collections import defaultdict

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        """
        since the swaps are unlimited.
        let an edge exist between each pair of numbers which are swappable.
        then sort each connected component based on nums[i] 
        
        """
        n = len(nums)
        arr = [[num, i, 0] for i, num in enumerate(nums)]
        arr.sort(key=lambda x: x[0])
        #arr = [[num, index_in_nums, component]]
        cur_comp = 0
        groups = defaultdict(list)
        groups[0].append((arr[0][0], arr[0][1]))

        for i in range(1, n):
            if abs(arr[i][0] - arr[i-1][0]) > limit:
                #start new component if out of reach
                cur_comp += 1
            groups[cur_comp].append((arr[i][0], arr[i][1]))

        #group indicies by component, sort each group 
        #and pari with values in that order
        result = [0]*n
        for pairs in groups.values():
            idxs = sorted(idx for _, idx in pairs)
            vals = [val for val, _ in pairs]  # already ascending, since arr was pre-sorted
            for idx, val in zip(idxs, vals):
                result[idx] = val
        

        return result



                

        
        

# @lc code=end
