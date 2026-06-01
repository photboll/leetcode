#
# @lc app=leetcode id=307 lang=python3
#
# [307] Range Sum Query - Mutable
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.st = [0] * (4*self.n)
        if self.n > 0:
            self.build(1, 0, self.n -1)

    def build(self, node, left, right):
        #leaf node
        if (left == right):
            self.st[node] = self.nums[left]
            return
        
        #  find middle element
        mid = (left + right) // 2
        # build left subtree
        self.build(2*node, left, mid)
        #build right subtree
        self.build(2 * node + 1, mid+1, right)
        #store the sum in the parent 
        self.st[node] = self.st[2*node] + self.st[2*node + 1]
        
        

    def update(self, index: int, val: int) -> None:
        self.update_helper(1, 0, self.n -1, index, val)

    def update_helper(self, node:int, left:int, right:int, index:int, val:int) -> None:
        #find the lead node and update it
        if left == right:
            self.nums[index] = val
            self.st[node] = val
            return
        
        mid = (left + right) //2

        # update the side that was affected by the change
        if index <= mid:
            self.update_helper(2 * node, left, mid, index, val)
        else:
            self.update_helper(2 * node+ 1, mid + 1, right, index, val)
        #update parent
        self.st[node] = self.st[2 * node] + self.st[2 * node +1]
        

    def sumRange(self, left: int, right: int) -> int:
        return self.query_helper(1, 0, self.n-1, left, right)
    
    def query_helper(self, node:int, node_left:int, node_right:int, left:int, right:int) -> int:
        if left == node_left and right == node_right: #exact match
            return self.st[node]
        
        mid = (node_left  + node_right) // 2
        if right <= mid:
            #fully to the left of mid
            return self.query_helper(2 * node, node_left, mid, left, right)
        elif left > mid:
            #fully to the right of mid
            return self.query_helper(2 * node + 1, mid + 1, node_right, left, right)
        else:
            #query spans both children
            return (
                self.query_helper(2 * node, node_left, mid, left, mid) +
                self.query_helper(2 * node+1, mid+1, node_right, mid+1, right)
            )

        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
# @lc code=end

