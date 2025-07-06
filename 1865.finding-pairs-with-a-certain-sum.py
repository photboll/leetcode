#
# @lc app=leetcode id=1865 lang=python3
#
# [1865] Finding Pairs With a Certain Sum
#

# @lc code=start
from collections import defaultdict

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.val2i = defaultdict(set)

        for i, v in enumerate(nums2):
            self.val2i[v].add(i)
        
        

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        new_val = old_val + val

        self.val2i[old_val].remove(index)
        self.val2i[new_val].add(index)
        self.nums2[index] = new_val
        

    def count(self, tot: int) -> int:
        count = 0
        for v in self.nums1:
            if tot - v in self.val2i:
                count += len(self.val2i[tot-v])
        return count 
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
# @lc code=end

