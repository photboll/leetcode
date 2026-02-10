#
# @lc app=leetcode id=3721 lang=python3
#
# [3721] Longest Balanced Subarray II
#

# @lc code=start
class SegmentTree:
    
    def __init__(self, n):
        self.n = n
        self.size = 4*n
        self.sum = [0] * self.size
        self.max = [0] * self.size
        self.min = [0] * self.size
    
    def _pull(self, node):
        """  helper to recompute information of node by it's children"""
        l, r = node *2, node*2 + 1
        self.sum[node] = self.sum[l] + self.sum[r]
        self.min[node] = min(self.min[l], self.sum[l] + self.min[r])
        self.max[node] = max(self.max[l] , self.sum[l] + self.max[r])
    
    def update(self, idx, val):
        "update valy of idx in original array"

        node, l, r = 1, 0, self.n-1
        path = []
        while l != r:
            path.append(node)
            m = l + (r - l) // 2
            if idx <= m:
                node = node*2
                r = m
            else:
                node = node*2+1
                l = m+1

        self.sum[node] = val
        self.min[node] = val
        self.max[node] = val
        while path:
            self._pull(path.pop())
    
    def find_rightmost_prefix(self, target):
        node, l, r, sum_before = 1, 0, self.n-1, 0

        def _exist(node, sum_before):
            return self.min[node] <= target - sum_before <= self.max[node]
        
        if not _exist(node, sum_before):
            return -1
        
        while l != r:
            m = l + (r - l) //2
            lchild, rchild = node * 2, node*2+1

            sum_before_right = self.sum[lchild] + sum_before
            if _exist(rchild, sum_before_right):
                node = rchild
                l = m+1
                sum_before = sum_before_right
            else:
                node = lchild
                r = m
        return l
    
        
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)

        stree = SegmentTree(n)
        #keep track of first occurenc 
        first = dict()

        result = 0

        for l in range(n-1, -1, -1):
            num = nums[l]

            #remove the old marker of x if we have already processed it earlier
            if num in first:
                stree.update(first[num], 0)
            
            #Now x is the first occurence 
            first[num] = l
            stree.update(l, 1 if num % 2 ==0 else -1)
            
            #find rightmost  r>= l such that the subarray is balanced
            r = stree.find_rightmost_prefix(target=0)
            if r >= l:
                result = max(result, r-l+1)

        return result

        
# @lc code=end

